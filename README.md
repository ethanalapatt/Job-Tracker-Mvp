# Job-Tracker-Mvp

# Job Tracker

A simple web application to track your job applications through different stages of the hiring process.

## Features

- Track job applications across 6 stages
- View statistics dashboard
- Add and update application details
- Track LinkedIn connections and scores
- Store job posting URLs
- Mark referral applications
- Dark theme interface

## Application Stages

1. **Making application** - Preparing your application
2. **Waiting for job to open** - Job not yet posted
3. **Applied** - Application submitted
4. **Accepted, Start Process** - Got the job!
5. **Rejected** - Application declined
6. **Waiting for a referral** - Need internal referral

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/job-tracker.git
cd job-tracker
```

2. Install Flask:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and go to `http://127.0.0.1:5000`

## Usage

### Adding Applications
1. Click "Add New Application"
2. Fill in company name and position
3. Select current stage
4. Add LinkedIn score and connections (optional)
5. Include job posting URL (optional)
6. Check referral box if applicable

### Updating Status
Use the colored buttons to quickly change application stages:
- Orange: Making application
- Purple: Waiting for job to open
- Blue: Applied
- Green: Accepted
- Red: Rejected
- Yellow: Waiting for referral

## Files

- `app.py` - Main Flask application
- `templates/base.html` - Base HTML template
- `templates/index.html` - Dashboard page
- `templates/add_job.html` - Add application form
- `jobs.db` - SQLite database (created automatically)

## Deployment

For free hosting, you can deploy to:
- Render
- Railway
- Fly.io
- PythonAnywhere

Add these files for deployment:
- `requirements.txt` with `Flask==2.3.3` and `gunicorn==21.2.0`
- `Procfile` with `web: gunicorn app:app`

## License

MIT License
