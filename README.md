# Lightweight-Personal-Productivity-Capture-Tool


## Overview

The **AI Personal Productivity Capture Tool** is a lightweight AI-powered web application that helps users capture daily tasks, notes, reminders, and to-do items using natural language.

The application uses **Google Gemini AI** to understand user input, extract actionable tasks, categorize them automatically, and store them in a local SQLite database. Users can manage their tasks through a simple dashboard and monitor their productivity.

---

## Features

- Capture tasks and notes using natural language
- AI-powered task extraction using Google Gemini API
- Automatic task categorization
  - Study
  - Work
  - Personal
- Automatic priority assignment
  - High
  - Medium
  - Low
- AI-generated note summary
- Store tasks in SQLite database
- Dashboard with productivity statistics
- View all tasks
- Mark tasks as completed
- Delete tasks
- Analytics based on task categories

---

## Technology Stack

- Python
- Flask
- HTML
- CSS
- SQLite
- Google Gemini API
- VS Code

---

## Project Structure

```
Lightweight-Personal-Productivity-Capture-Tool/
│
├── app.py
├── database.py
├── gemini.py
├── task.db
├── .env
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── capture.html
│   ├── tasks.html
│   └── analytics.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

## Project Workflow

```
User Input
      │
      ▼
Capture Page
      │
      ▼
Google Gemini AI
      │
      ▼
Extract Tasks
Categorize Tasks
Generate Summary
      │
      ▼
SQLite Database
      │
      ▼
Dashboard
      │
      ▼
Task Management & Analytics
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/adwaithpramod994/Lightweight-Personal-Productivity-Capture-Tool.git
```

### Open Project

```bash
cd Lightweight-Personal-Productivity-Capture-Tool
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run the Project

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## Modules

### Dashboard

Displays:

- Total Tasks
- Completed Tasks
- Pending Tasks
- Productivity Progress

---

### Capture

Allows users to enter tasks or notes in natural language.

Example:

```
Complete AI project today.
Prepare for Java interview tomorrow.
Buy groceries.
```

---

### AI Processing

Google Gemini API performs:

- Task Extraction
- Task Categorization
- Priority Assignment
- Note Summarization

---

### Task Management

Users can:

- View Tasks
- Complete Tasks
- Delete Tasks

---

### Analytics

Displays:

- Tasks by Category
- Completed Tasks
- Pending Tasks

---

## Future Enhancements

- Voice-to-Task Conversion
- User Authentication
- Cloud Database Integration
- Calendar Integration
- Email & Push Notifications
- Due Date Detection
- Smart Productivity Insights
- Mobile Responsive Design

---

## Learning Outcomes

- Flask Web Development
- REST Routing
- SQLite Database Operations
- Google Gemini API Integration
- Prompt Engineering
- CRUD Operations
- AI-assisted Productivity Applications

---

## Developed By

**Adwaith Pramod**

GitHub:
https://github.com/adwaithpramod994

---

## License

This project is developed for educational and hackathon purposes.
