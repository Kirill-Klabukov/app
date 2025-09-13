# app

A lightweight Python web application that works with student data stored in a JSON file.

## Overview
The project provides a simple way to read and serve student information through a web interface or API.  
It is designed as a starting point for small projects and educational purposes.

## Structure
- `app.py` — main application file (entry point).  
- `students.json` — dataset with student information.  
- `requirements.txt` — dependencies needed to run the project.  
- `Procfile` — startup file for deployment platforms (e.g. Heroku).  
- `templates/` — optional HTML templates for rendering views.  

## Features
- Reads data directly from a JSON file.  
- Serves content via HTTP endpoints.  
- Minimal dependencies, quick to set up.  
- Deployment-ready configuration.  

## Installation & Run
```bash
git clone https://github.com/Kirill-Klabukov/app.git
cd app
pip install -r requirements.txt
python app.py
