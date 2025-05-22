import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# Configuration
SHEET_ID = "1XxX5ScIUJvv7m4q9fW7iuH3N_P0TExUPha9hMNZxSqA"
MOODS = {
    "😊 Happy": "Happy",
    "😠 Frustrated": "Frustrated",
    "😕 Confused": "Confused", 
    "🎉 Excited": "Excited",
    "😴 Tired": "Tired"
    ## More moods can be added here
}
MOOD_COLORS = {
    'Excited': '#8CD17D',  # Light green
    'Happy': '#F9E79F',    # Light yellow
    'Frustrated': '#C7B8E6', # Light purple
    'Confused': '#F1948A',  # Light red/pink
    'Tired': '#85C1E9'      # Light blue
            }
# Page configuration
st.set_page_config(page_title="Mood of the Queue", page_icon="😃", layout="wide")

# Connect to Google Sheets
def init_sheets():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    
    try:
        if os.path.exists('credentials.json'):
            creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        elif 'gcp_service_account' in st.secrets:
            creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets['gcp_service_account'], scope)
        else:
            st.error("No credentials found!")
            st.stop()
        
        client = gspread.authorize(creds)
        return client.open_by_key(SHEET_ID).sheet1
    except Exception as e:
        st.error(f"Error connecting to Google Sheets: {str(e)}")
        return None

# Initialize session
if 'sheet' not in st.session_state:
    st.session_state.sheet = init_sheets()

# Load data
try:
    data = pd.DataFrame(st.session_state.sheet.get_all_records())
    if not data.empty:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')
        data = data.dropna(subset=['Timestamp'])
        data['Date'] = data['Timestamp'].dt.date
except Exception as e:
    data = pd.DataFrame()
    st.error(f"Error loading data: {str(e)}")

# App layout - Two columns
left_col, right_col = st.columns([1, 3])

# LEFT COLUMN - Log a Mood
with left_col:
    st.header("Log a Mood")
    
    mood = st.selectbox("How's the queue feeling?", list(MOODS.keys()))
    note = st.text_area("Add a note (optional)", max_chars=500, help="Maximum 100 words")
    
    if st.button("Submit Mood"):
        try:
            st.session_state.sheet.append_row([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                MOODS[mood], 
                note
            ])
            st.success("Mood logged!")
            # Refresh data
            data = pd.DataFrame(st.session_state.sheet.get_all_records())
            if not data.empty:
                data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')
                data = data.dropna(subset=['Timestamp'])
                data['Date'] = data['Timestamp'].dt.date
        except Exception as e:
            st.error(f"Error: {str(e)}")
    
    # Recent Entries section
    if not data.empty:
        st.subheader("Recent Entries")
        recent_entries = data.sort_values('Timestamp', ascending=False).head(10)
        
        entries_df = recent_entries[['Timestamp', 'Mood', 'Note']].copy()
        entries_df['Timestamp'] = entries_df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
        
        st.dataframe(
            entries_df, 
            hide_index=True,
            height=300,
            use_container_width=True
        )

# RIGHT COLUMN - Visualization
with right_col:
    if data.empty:
        st.info("No mood entries yet. Start logging moods!")
    else:
        dates = sorted(data['Date'].unique(), reverse=True)
        
        if dates:
            st.title("😃⏳ Mood of the Queue")
            
            selected_date = st.selectbox(
                "Choose a date to view",
                options=dates,
                format_func=lambda x: x.strftime("%Y-%m-%d")
            )
            
            daily_data = data[data['Date'] == selected_date]
            
            if not daily_data.empty:
                # Mood stats
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("Most Common Mood (Selected Date)")
                    day_mood = daily_data['Mood'].mode().iloc[0]
                    st.markdown(f"## {day_mood}")
                
                with col2:
                    st.write("Most Common Mood (Selected Week)")
                    week_start = selected_date - timedelta(days=selected_date.weekday())
                    week_end = week_start + timedelta(days=6)
                    week_data = data[(data['Date'] >= week_start) & (data['Date'] <= week_end)]
                    if not week_data.empty:
                        week_mood = week_data['Mood'].mode().iloc[0]
                        st.markdown(f"## {week_mood}")
                
                # Mood Distribution chart
                st.subheader("Mood Distribution")
                
                mood_counts = daily_data['Mood'].value_counts().reset_index()
                mood_counts.columns = ['Mood', 'Count']
                
                fig = px.bar(
                    mood_counts,
                    x='Mood', 
                    y='Count',
                    color='Mood',
                    color_discrete_map=MOOD_COLORS,
                    text='Count'
                )
                
                fig.update_layout(
                    showlegend=False,
                    xaxis_title="",
                    yaxis_title="Count"
                )
                
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info(f"No mood entries for {selected_date.strftime('%Y-%m-%d')}")
        else:
            st.info("No valid dates found in the data.")

# Auto-refresh
st.markdown("---")
st.markdown("🔄 Auto-refreshing every 30 seconds...")
st.empty() 