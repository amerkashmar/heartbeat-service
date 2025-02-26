# Heartbeat Service

A simple service that sends a GET request to `https://api.kmt.ltd/api/Auth/heartbeat` every 2 minutes.

## Local Usage

1. Install dependencies:
   ```
   pip install -r requirements_heartbeat.txt
   ```

2. Run the script:
   ```
   python heartbeat.py
   ```

## Free Hosting Options

### 1. GitHub Actions (Recommended for simplicity)

The easiest and most reliable free option:

1. Create a GitHub repository and push this code to it.
2. The `.github/workflows/heartbeat.yml` file is already set up to run every 2 minutes.
3. GitHub Actions will automatically execute the workflow according to the schedule.
4. This method uses GitHub's servers and doesn't require any additional accounts.

### 2. Heroku

Heroku offers a free tier that can run this script:

1. Create a Heroku account at https://signup.heroku.com/
2. Install the Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
3. Login and create a new app:
   ```
   heroku login
   heroku create your-heartbeat-app
   ```
4. Push your code to Heroku:
   ```
   git init
   git add .
   git commit -m "Initial commit"
   heroku git:remote -a your-heartbeat-app
   git push heroku main
   ```
5. Scale the worker dyno:
   ```
   heroku ps:scale worker=1
   ```

### 3. Railway

Railway offers a free tier with generous limits:

1. Sign up at https://railway.app/
2. Create a new project and connect your GitHub repository
3. Railway will automatically detect and deploy your Python application
4. The service will run continuously

### 4. PythonAnywhere

PythonAnywhere offers a free tier that can run scheduled tasks:

1. Create an account at https://www.pythonanywhere.com/
2. Upload your `heartbeat.py` file
3. Set up a scheduled task to run every 2 minutes

### 5. Google Cloud Run

Google Cloud offers a free tier:

1. Create a Google Cloud account
2. Build and deploy the Docker container:
   ```
   gcloud builds submit --tag gcr.io/YOUR-PROJECT-ID/heartbeat
   gcloud run deploy --image gcr.io/YOUR-PROJECT-ID/heartbeat --platform managed
   ```
3. Set up Cloud Scheduler to invoke the service every 2 minutes

## Notes

- Most free tiers have limitations on uptime or usage, so check the terms of service.
- GitHub Actions is the simplest solution as it doesn't require maintaining a server.
- For long-term reliability, consider a low-cost VPS like DigitalOcean ($5/month) or a Raspberry Pi at home.
