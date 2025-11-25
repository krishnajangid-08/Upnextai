🧠 UpNext AI
AI-Powered Resume Intelligence & Skill Gap Analyzer

Transform your resume into actionable career insights.

UpNext AI is a modern AI-driven web platform that analyzes resumes using the Google Gemini 2.5 Pro model and delivers deep insights such as skill extraction, missing skills, summary recommendations, and job intelligence. Built with clean UI/UX and robust backend logic, it provides a seamless and professional experience from upload to analysis.

📌 Table of Contents

Features

Live Demo

Screenshots

Architecture

Tech Stack

Project Structure

How It Works

Setup Instructions

Environment Variables

Future Roadmap

Contributors

License

🚀 Features
🎯 AI Resume Analysis

Uses Gemini 2.5 Pro to extract:

Skills found in resume

Missing skills based on job market

Professional AI summary

Job recommendations based on your skill stack

🖥️ Modern & Futuristic UI/UX

Blue-white gradient theme

Neon glow elements

Smooth animations (fade, slide, scroll reveal)

Mobile responsive design

Polished upload → analyzing → results flow

📦 Fail-Safe Fallback Mode

If the Google API cannot be reached:

Default skills

Default missing skills

Default summary
Ensures the app never breaks.

📄 Resume Preview

Shows extracted text from the PDF
Helps verify if OCR/data extraction worked properly.

💼 Smart Job Recommendations

Recommends roles based on extracted skills:

AI Product Analyst

Data Storytelling Lead

Skill Intelligence Consultant
…and more.

🏗️ Architecture

                ┌────────────────────────┐
                │        Browser         │
                │ (User Uploads Resume)  │
                └──────────┬─────────────┘
                           │ POST /upload
                           ▼
              ┌─────────────────────────────┐
              │           Flask API          │
              │     (app.py - Backend)       │
              └──────────┬─────────────┬────┘
                         │             │
                 Extract PDF       Build Prompt
               (PyPDF2 Library)   (Resume Text)
                         │             │
                         └──────┬──────┘
                                ▼
                 ┌─────────────────────────┐
                 │  Google Gemini API      │
                 │   (Skill Analysis)      │
                 └──────────┬──────────────┘
                            │ JSON Response
                            ▼
               ┌─────────────────────────────┐
               │ Frontend Result Renderer     │
               │  (HTML/CSS/JS Templates)     │
               └────
               ─────────────────────────┘
📁 Project Structure


ai_job_skill_platform/
│
├── app.py                     # Main backend logic
├── templates/
│   ├── index.html             # Homepage
│   ├── upload.html            # Upload & analyzing UI
│   └── result.html            # Final results page
│
├── static/
│   ├── style.css              # UI styling + animations
│   ├── logo.png               # UpNext AI logo
│   └── favicon.png            # Site favicon
│
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Excluded files
🧩 Tech Stack
Frontend

HTML5

CSS3 + Animations

JavaScript

Backend

Python

Flask

PyPDF2

AI Model

Google Gemini 2.5 Pro
Via the Generative Language API

Version Control

Git & GitHub

🛠️ How It Works (Short & Clear)

User uploads a PDF resume.

Text is extracted using PyPDF2.

The cleaned text is fed to Gemini 2.5 Pro.

AI returns structured JSON:

skills_found

missing_skills

summary

Frontend displays results with animations.

If AI fails → fallback mode activates.

🔧 Setup Instructions (Run Locally)
1. Clone the Repo
git clone https://github.com/YOUR_USERNAME/upnext-ai.git
cd upnext-ai

2. Create Virtual Env
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Add API Key

Create .env:

GEMINI_API_KEY=your_actual_key_here

5. Run Flask
python app.py


Open:
👉 http://127.0.0.1:5000/

🔐 Environment Variables
Key	Description
GEMINI_API_KEY	Google Gemini API key
🛣️ Future Roadmap (Makes your project look BIG & PROFESSIONAL)
✓ Planned Enhancements

ATS score calculator

Skill confidence scoring

Job-role match percentage

Resume rewriting suggestions

LinkedIn-style profile generation

Email export (PDF report)

OCR for image-based resumes

Database integration (MongoDB / PostgreSQL)

User accounts + dashboard

👥 Contributors

Krishna Jangid
Developer – AI & Web Engineering
UpNext AI © 2025

📜 License

This project is licensed for educational and research purposes.
