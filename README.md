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
   - Set up Google API credentials
   - Share sheet with the service account email
   - Update `GOOGLE_SHEET_ID` in app.py

3. **Credentials Setup**
   - For local development: Save service account JSON as `credentials.json` (not tracked by git)
   - For Streamlit deployment: Add credentials to Streamlit secrets (see Deployment section)

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

## Usage
- **Logging**: Select mood and add optional note in sidebar
- **Viewing**: Charts show distribution by day with weekly summaries
- **Filtering**: Use date picker to view historical data

## Deployment
Deploy to Streamlit Cloud by connecting your GitHub repo:

1. Store credentials securely using Streamlit secrets:
   - Go to your app's dashboard on Streamlit Cloud
   - Navigate to App settings > Secrets
   - Add your credentials in this format:
     ```toml
     [gcp_service_account]
     type = "service_account"
     project_id = "your-project-id"
     private_key_id = "your-private-key-id"
     private_key = "your-private-key"
     client_email = "your-client-email"
     client_id = "your-client-id"
     auth_uri = "https://accounts.google.com/o/oauth2/auth"
     token_uri = "https://oauth2.googleapis.com/token"
     auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
     client_x509_cert_url = "your-cert-url"
     ```

2. NEVER commit credentials to your repository.

The app is deployed at: https://eugenekim90-mood-tracker-app-auh1tk.streamlit.app/

## Project Files
- `app.py`: Main application
- `requirements.txt`: Dependencies
- `credentials.json`: API credentials (not in repo)

