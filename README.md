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
   - Place credentials.json in the root directory
   - Update `GOOGLE_SHEET_ID` in app.py with your sheet ID

3. **Run the App**
   ```bash
   streamlit run app.py
   ```

## Usage
- **Logging**: Select mood and add optional note in sidebar
- **Viewing**: Charts show distribution by day with weekly summaries
- **Filtering**: Use date picker to view historical data

## Deployment
For deployment to Streamlit Cloud:

1. In Streamlit Cloud, go to your app settings → Secrets
2. Add a new secret called `gcp_credentials`
3. Copy and paste the **entire JSON content** from your credentials.json file:
   ```
   {
     "type": "service_account",
     "project_id": "your-project-id",
     "private_key_id": "your-private-key-id",
     "private_key": "your-private-key",
     ...rest of your credentials file...
   }
   ```
4. The app will automatically use these credentials when deployed

The app is deployed at: https://eugenekim90-mood-tracker-app-auh1tk.streamlit.app/

## Project Files
- `app.py`: Main application
- `requirements.txt`: Dependencies
- `credentials.json`: Google API credentials (not in repo)

