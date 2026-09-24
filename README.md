
# Student Notes Management System

A Flask-based web application that allows users to securely manage their notes, upload and download files, and organize their study materials through a simple web interface.

## 🚀 Live Demo

[Student Notes Management System](https://student-notes-management-system-2-6cbn.onrender.com/)

## ✨ Features

- User Registration and Login
- OTP-Based Email Verification
- Secure User Authentication
- Add, View, Update, and Delete Notes
- File Upload and Download
- Search Notes
- Export Notes to Excel
- MySQL Database Integration
- Cloud Deployment using Render

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask-Bcrypt
- Flask-Session
- MySQL Connector/Python

### Database
- MySQL
- Aiven Cloud MySQL

### Frontend
- HTML
- CSS

### Email and Deployment
- Gmail SMTP
- Render

## 📁 Project Features

### User Authentication
- User registration with email verification
- Login and logout functionality
- Password hashing using Flask-Bcrypt
- Session-based authentication

### Notes Management
- Create new notes
- View saved notes
- Update existing notes
- Delete notes
- Search notes

### File Management
- Upload files
- Download stored files
- Export notes to Excel

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/manojkumarbathula/student-notes-management-system.git
cd student-notes-management-system
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file and configure the required database and email environment variables.

Do not commit `.env` or passwords to GitHub.

### 5. Run the Application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000/
```

## ☁️ Deployment

The application is deployed on Render and uses Aiven Cloud MySQL as its database.

- Application Hosting: Render
- Database Hosting: Aiven Cloud MySQL
- Email Service: Gmail SMTP
- Database Connection: SSL-secured MySQL connection

## 🔐 Security Considerations

- Passwords are hashed using Flask-Bcrypt.
- Sensitive credentials are stored using environment variables.
- Gmail App Passwords are not stored directly in the source code.
- Database credentials are managed through environment variables.

## 👨‍💻 Author

**Manoj Kumar Bathula**

GitHub: [manojkumarbathula](https://github.com/manojkumarbathula)
