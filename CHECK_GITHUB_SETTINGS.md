# GitHub Actions Scheduling Checklist

## Repository Settings to Check

1. **Repository Visibility**
   - Public repositories have fewer restrictions for GitHub Actions
   - If your repository is private, consider making it public (if it doesn't contain sensitive information)

2. **Branch Protection**
   - Check if your main branch has protection rules that might interfere with Actions
   - Go to Settings → Branches → Branch protection rules

3. **Actions Permissions**
   - Go to Settings → Actions → General
   - Ensure "Allow all actions and reusable workflows" is selected
   - Set "Workflow permissions" to "Read and write permissions"

## Workflow File Validation

1. **Indentation and Syntax**
   - YAML files are sensitive to indentation
   - Ensure there are no syntax errors in your workflow file

2. **Cron Syntax**
   - GitHub uses UTC time for cron schedules
   - The format `*/2 * * * *` should run every 2 minutes

## Common Issues with Scheduled Workflows

1. **Initial Delay**
   - New or modified scheduled workflows can take up to an hour to start running
   - GitHub needs time to register the schedule

2. **GitHub's Infrastructure Load**
   - Scheduled workflows might be delayed during periods of high load
   - Delays of up to 15 minutes are not uncommon

3. **Repository Activity**
   - GitHub may disable scheduled workflows for inactive repositories
   - Regular commits or manual workflow runs can keep the repository active

## Alternative Approach

If scheduled workflows continue to be unreliable, consider using a different approach:

```yaml
name: Heartbeat Service

on:
  workflow_dispatch:
  push:
    branches: [ main ]

jobs:
  heartbeat:
    runs-on: ubuntu-latest
    
    steps:
    - name: Initial heartbeat
      run: |
        curl -s -X GET https://api.kmt.ltd/api/Auth/heartbeat
        echo "Initial heartbeat sent at $(date)"
        
    - name: Schedule next run
      run: |
        # Create a new workflow dispatch event in 2 minutes
        sleep 120
        curl -X POST \
          -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
          -H "Accept: application/vnd.github.v3+json" \
          https://api.github.com/repos/${{ github.repository }}/actions/workflows/heartbeat.yml/dispatches \
          -d '{"ref":"main"}'
```

This approach uses the workflow to trigger itself after a delay, creating a loop. However, it requires setting up a Personal Access Token with workflow permissions.
