# AI Skill Gap Analyzer

An AI-powered web application that analyzes a job description, identifies the required technical skills, compares them with the user's skills, and generates a personalized learning roadmap.

## 🚀 Live Demo
## 🚀 Live Demo

[Open Skill Gap Analyzer](https://skill-gap-analyzer-gtvl.onrender.com)

## ✨ Features

- Extracts required technical skills from job descriptions
- Compares required skills with user's existing skills
- Identifies missing skills
- Generates a personalized learning roadmap
- Provides beginner-friendly learning suggestions
- AI-powered analysis using OpenAI API
- Responsive web interface

## 🛠️ Tech Stack

- Python
- Flask
- JavaScript
- HTML
- CSS
- OpenAI API
- Gunicorn

## 🔄 How It Works

1. User enters a job description.
2. User enters their existing technical skills.
3. The application sends the information to the Flask backend.
4. OpenAI analyzes the job description and extracts required skills.
5. The application compares required skills with the user's skills.
6. Missing skills are identified.
7. AI generates a learning roadmap for the missing skills.

## 📁 Project Structure

```text
skill-gap-analyzer/
│
├── app.py
├── requirements.txt
├── test_api.py
├── .gitignore
│
├── static/
│   ├── script.js
│   └── styles.css
│
└── templates/
    └── index.html
