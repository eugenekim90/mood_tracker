# Mood of the Queue

A simple tool for tracking and visualizing support ticket queue moods.

## Features
- Log moods with emojis and optional notes
- Interactive mood distribution charts 
- Daily/weekly mood trends
- Auto-refresh and date filtering

## Quick Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Google Sheet Setup**
   - Create a Google Sheet with columns: Timestamp, Mood, Note
   - Create a Google Cloud service account and download credentials.json
   - Share your sheet with the service account email


3. **Run the App**
   ```bash
   streamlit run app.py
   ```

## Usage
- **Logging**: Select mood and add optional note in sidebar
- **Viewing**: Charts show distribution by day with weekly summaries
- **Filtering**: Use date picker to view historical data

## Project Files
- `app.py`: Main application
- `requirements.txt`: Dependencies
- `credentials.json`: Google API credentials (not included in repo, optional if using Streamlit secrets)

