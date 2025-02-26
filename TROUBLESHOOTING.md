# Troubleshooting GitHub Actions Scheduled Workflows

If your scheduled GitHub Actions workflows are not running automatically, here are some common issues and solutions:

## Common Issues

1. **Delayed Execution**
   - GitHub Actions scheduled workflows can be delayed by up to 15 minutes during periods of high load.
   - Be patient and check back after some time.

2. **Repository Inactivity**
   - GitHub may disable scheduled workflows in repositories that have been inactive.
   - Manually trigger the workflow to reactivate it.

3. **Schedule Syntax**
   - Ensure your cron syntax is correct.
   - GitHub Actions uses UTC time for cron schedules.

4. **Workflow File Location**
   - Make sure your workflow file is in the `.github/workflows/` directory.
   - Ensure the file has a `.yml` or `.yaml` extension.

5. **Default Branch**
   - Scheduled workflows only run on the default branch of your repository.
   - Ensure your workflow file is on the `main` branch (or whatever your default branch is).

## Verification Steps

1. **Check Actions Tab**
   - Go to the "Actions" tab in your repository.
   - Look for any error messages or failed runs.

2. **Manual Trigger**
   - Manually trigger the workflow to verify it works.
   - If manual triggering works but scheduled runs don't, it's likely a scheduling issue.

3. **Check Repository Settings**
   - Go to Settings > Actions > General
   - Ensure Actions are enabled for your repository.

4. **Wait After Changes**
   - After pushing changes to a workflow file, GitHub needs time to register the schedule.
   - Wait up to an hour for the scheduled workflow to start running automatically.

## GitHub Actions Limitations

- **Frequency**: GitHub Actions doesn't support running workflows more frequently than once per minute.
- **Free Tier**: Free accounts have 2,000 minutes per month of GitHub Actions usage.
- **Concurrent Jobs**: Free accounts can run up to 20 concurrent jobs.

## Next Steps

If you've tried all the above and your scheduled workflow still isn't running:

1. Check the GitHub Status page (https://www.githubstatus.com/) for any ongoing issues.
2. Consider creating a new workflow file with a simpler configuration to test if scheduling works.
3. Contact GitHub Support if the issue persists.
