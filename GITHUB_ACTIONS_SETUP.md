# GitHub Actions Setup Instructions

To ensure your scheduled workflows run properly, please check the following GitHub repository settings:

## 1. Enable GitHub Actions

1. Go to your repository on GitHub
2. Click on "Settings" tab
3. In the left sidebar, click on "Actions" → "General"
4. Under "Actions permissions", make sure "Allow all actions and reusable workflows" is selected
5. Scroll down and click "Save"

## 2. Check Workflow Permissions

1. While still in the Actions settings page
2. Scroll down to "Workflow permissions"
3. Select "Read and write permissions"
4. Check "Allow GitHub Actions to create and approve pull requests"
5. Click "Save"

## 3. Alternative Approaches

If scheduled workflows still aren't running after checking the settings, here are some alternative approaches:

### Option 1: Use a different hosting service

1. **Render.com** - Free tier with background workers
   - Sign up at render.com
   - Create a new "Background Worker" service
   - Point it to your GitHub repository
   - Set the start command to `python heartbeat.py`

2. **Railway.app** - Free tier with automatic deployments
   - Sign up at railway.app
   - Connect your GitHub repository
   - Set the start command to `python heartbeat.py`

### Option 2: Use a GitHub webhook

1. Create a webhook in your repository settings
2. Set it to trigger on a schedule using an external service like cron-job.org
3. The webhook can then trigger your workflow

### Option 3: Use GitHub Actions with a different approach

1. Instead of using the `schedule` trigger, create a workflow that runs continuously with sleep:

```yaml
name: Continuous Heartbeat

on:
  workflow_dispatch:
  push:
    branches: [ main ]

jobs:
  heartbeat:
    runs-on: ubuntu-latest
    
    steps:
    - name: Continuous heartbeat
      run: |
        while true; do
          curl -X GET https://api.kmt.ltd/api/Auth/heartbeat
          echo "Heartbeat sent at $(date)"
          sleep 120  # Wait 2 minutes
        done
```

Note: This approach will use up your GitHub Actions minutes more quickly.
