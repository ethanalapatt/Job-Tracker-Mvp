# =============================================================================
# app.py
# =============================================================================

import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Database setup
def init_db():
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            stage TEXT NOT NULL,
            linkedin_score REAL DEFAULT 1.0,
            num_connections INTEGER DEFAULT 0,
            apply_date DATE,
            response_date DATE,
            posting_url TEXT,
            referral BOOLEAN DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Database operations
def get_all_applications():
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, company, position, stage, linkedin_score, num_connections, 
               apply_date, response_date, posting_url, referral
        FROM applications 
        ORDER BY apply_date DESC
    ''')
    apps = cursor.fetchall()
    conn.close()
    return apps

def add_application(company, position, stage, linkedin_score=1.0, num_connections=0, 
                   apply_date=None, response_date=None, posting_url='', referral=False):
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    
    if apply_date == '':
        apply_date = None
    if response_date == '':
        response_date = None
        
    cursor.execute('''
        INSERT INTO applications (company, position, stage, linkedin_score, num_connections,
                                apply_date, response_date, posting_url, referral)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (company, position, stage, linkedin_score, num_connections, 
          apply_date, response_date, posting_url, referral))
    
    conn.commit()
    conn.close()

def update_application_stage(app_id, new_stage):
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE applications SET stage = ? WHERE id = ?', (new_stage, app_id))
    conn.commit()
    conn.close()

def get_stage_counts():
    conn = sqlite3.connect('jobs.db')
    cursor = conn.cursor()
    cursor.execute('SELECT stage, COUNT(*) FROM applications GROUP BY stage')
    counts = dict(cursor.fetchall())
    conn.close()
    return counts

# Routes
@app.route('/')
def index():
    applications = get_all_applications()
    stage_counts = get_stage_counts()
    return render_template('index.html', applications=applications, stage_counts=stage_counts)

@app.route('/add', methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        company = request.form['company']
        position = request.form['position']
        stage = request.form['stage']
        linkedin_score = float(request.form.get('linkedin_score', 1.0))
        num_connections = int(request.form.get('num_connections', 0))
        apply_date = request.form.get('apply_date')
        response_date = request.form.get('response_date')
        posting_url = request.form.get('posting_url', '')
        referral = 'referral' in request.form
        
        add_application(company, position, stage, linkedin_score, num_connections,
                       apply_date, response_date, posting_url, referral)
        flash('Application added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_job.html')

@app.route('/update_stage/<int:app_id>/<new_stage>')
def update_stage(app_id, new_stage):
    update_application_stage(app_id, new_stage)
    flash(f'Stage updated to {new_stage}', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
