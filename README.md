# Mood of the Queue

A simple Streamlit app for tracking the emotional state of support queues.

## Features

- 😊 Log mood entries with emoji options (Happy, Frustrated, Confused, Excited, Tired)
- 📊 Visualize mood distributions
- 📅 Track weekly trends and most common moods
- 📝 Add optional notes to each mood entry
- 🔄 Auto-refreshing data display

## Setup

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up Google Sheets API:
   - Create a service account and download `credentials.json`
   - Share your Google Sheet with the service account email
   
3. Configure authentication:
   - Place `credentials.json` in the project root directory
   - OR create `.streamlit/secrets.toml` with your service account credentials

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Log Moods**: Select an emoji that represents the current queue feeling and add an optional note
2. **View Recent Entries**: See the 10 most recent mood entries directly in the left sidebar
3. **Analyze Trends**: 
   - Select a date from the dropdown to view mood distribution for that day
   - See the most common mood for both the selected date and its containing week
   - Visualize distribution with the color-coded bar chart
4. **Filter Data**: Use the date selector to view historical data and track mood patterns over time



