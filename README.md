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

## Data Structure

The Google Sheet should have the following columns:
- `Timestamp` (YYYY-MM-DD HH:MM:SS)
- `Mood` (Happy, Frustrated, Confused, Excited, Tired)
- `Note` (optional)

# Update 1
