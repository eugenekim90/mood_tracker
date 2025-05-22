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

## Deployment to Streamlit Cloud

1. **Add your credentials to Streamlit Secrets**:
   - In Streamlit Cloud, go to your app settings → Secrets
   - Add the following, replacing with your actual credentials:
     ```
     gcp_service_account = """
     {
       "type": "service_account",
       "project_id": "your-project-id",
       "private_key_id": "your-key-id",
       "private_key": "-----BEGIN PRIVATE KEY-----\n...",
       "client_email": "your-service-account@your-project.iam.gserviceaccount.com",
       "client_id": "your-client-id",
       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
       "token_uri": "https://oauth2.googleapis.com/token",
       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
       "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account"
     }
     """
     ```
   - Make sure to paste your entire credentials.json content as a single string between the triple quotes

2. **Deploy your app**:
   - Connect your GitHub repository to Streamlit Cloud
   - Set the main file path to `app.py`

## Project Files
- `app.py`: Main application
- `requirements.txt`: Dependencies
- `credentials.json`: Google API credentials (local only, not in repo)
- `.streamlit/secrets.toml`: Template for Streamlit secrets

