import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

# Google Sheet ID
GOOGLE_SHEET_ID = "1XxX5ScIUJvv7m4q9fW7iuH3N_P0TExUPha9hMNZxSqA"

# Define moods with emojis
MOODS = {
    "😊 Happy": "Happy",
    "😠 Frustrated": "Frustrated",
    "😕 Confused": "Confused", 
    "🎉 Excited": "Excited",
    "😴 Tired": "Tired"
}

# Set page config
st.set_page_config(
    page_title="Mood of the Queue",
    page_icon="😃⏳",
    layout="wide"
)

# Initialize Google Sheets connection
def init_gsheets():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    
    # First try to get credentials from Streamlit secrets as text
    try:
        if 'gcp_credentials' in st.secrets:
            # Create a credentials.json file from the secret
            credentials_dict = json.loads(st.secrets['gcp_credentials'])
            credentials = ServiceAccountCredentials.from_json_keyfile_dict(
                credentials_dict, scope)
        else:
            # Check if credentials file exists locally
            if not os.path.exists('credentials.json'):
                st.error("credentials.json file not found!")
                st.info("Please create credentials.json locally or add a 'gcp_credentials' secret in Streamlit Cloud.")
                st.stop()
            
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                'credentials.json', scope)
        
        client = gspread.authorize(credentials)
        sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1
        return sheet
    except Exception as e:
        st.error(f"Error accessing Google Sheet: {str(e)}")
        st.stop()

# Initialize session state
if 'sheet' not in st.session_state:
    try:
        st.session_state.sheet = init_gsheets()
    except Exception as e:
        st.error(f"Error connecting to Google Sheets: {str(e)}")
        st.stop()

# Sidebar for mood input
st.sidebar.title("Log a Mood")
selected_mood = st.sidebar.selectbox("How's the queue feeling?", list(MOODS.keys()))
note = st.sidebar.text_area("Add a note (optional)")

if st.sidebar.button("Submit Mood"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mood = MOODS[selected_mood]
    try:
        st.session_state.sheet.append_row([timestamp, mood, note])
        st.sidebar.success("Mood logged successfully!")
    except Exception as e:
        st.sidebar.error(f"Error logging mood: {str(e)}")

# Main content area
st.title("😃⏳ Mood of the Queue")

# Get data from Google Sheets
try:
    data = pd.DataFrame(st.session_state.sheet.get_all_records())
    if data.empty:
        st.info("No mood entries yet. Start logging moods using the sidebar!")
    else:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
        data['Date'] = data['Timestamp'].dt.date
        
        # Create two columns
        col1, col2 = st.columns([1, 2])
        
        with col2:
            selected_date = st.date_input(
                "Choose a date to view",
                value=datetime.now().date(),
                min_value=data['Date'].min(),
                max_value=datetime.now().date()
            )
            
            # Filter data for selected date
            daily_data = data[data['Date'] == selected_date]
            if not daily_data.empty:
                # Create mood count chart
                mood_counts = daily_data['Mood'].value_counts().reset_index()
                mood_counts.columns = ['Mood', 'Count']
                
                fig = px.bar(
                    mood_counts,
                    x='Mood',
                    y='Count',
                    title="Mood Distribution",
                    color='Mood',
                    color_discrete_sequence=px.colors.qualitative.Set3
                )
                fig.update_layout(
                    showlegend=False,
                    xaxis_title="",
                    yaxis_title="Count",
                    height=400
                )
                fig.update_yaxes(tickformat="d")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info(f"No mood entries for {selected_date}")
        
        with col1:
            if not daily_data.empty:
                # Show summary statistics
                day_mood = daily_data['Mood'].mode().iloc[0]
                st.metric("Most Common Mood (Today)", day_mood)
                
                # Most common mood for the week
                week_start = selected_date - timedelta(days=selected_date.weekday())
                week_end = week_start + timedelta(days=6)
                week_data = data[(data['Date'] >= week_start) & (data['Date'] <= week_end)]
                if not week_data.empty:
                    week_mood = week_data['Mood'].mode().iloc[0]
                    st.metric("Most Common Mood (This Week)", week_mood)
                
                # Show entries for selected date
                st.subheader("Recent Entries")
                date_entries = daily_data.sort_values('Timestamp', ascending=False)
                st.dataframe(
                    date_entries[['Timestamp', 'Mood', 'Note']],
                    hide_index=True,
                    height=200
                )
except Exception as e:
    st.error(f"Error loading data: {str(e)}")

# Add auto-refresh
st.empty()
st.markdown("---")
st.markdown("🔄 Auto-refreshing every 30 seconds...")
st.empty() 