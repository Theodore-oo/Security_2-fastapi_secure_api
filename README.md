🔐 Secure FastAPI ERP-Style API

A production-ready secure REST API built with FastAPI, featuring:

✅ JWT Authentication

✅ Password Hashing (bcrypt)

✅ Role-Based Access Ready

✅ SQLite Database

✅ Protected Routes

✅ Swagger Documentation

This project is designed for Backend + Application Security practice.

🚀 Tech Stack

FastAPI

Uvicorn

SQLite

SQLAlchemy ORM

JWT (python-jose)

Passlib (bcrypt)


⚙️ Installation

1️⃣ Clone Repository
git clone https://github.com/yourusername/fastapi-secure-api.git
cd fastapi-secure-api

2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac

Windows:
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the Server
uvicorn app.main:app --reload

Open in browser:
http://127.0.0.1:8000/docs

Swagger UI will be available automatically 🎉

🔑 Authentication Flow
Register User
POST /register

{
  "username": "admin",
  "password": "password123"
}

Login
POST /login

{
  "username": "admin",
  "password": "password123"
}

Response:
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
Access Protected Route

Click Authorize in Swagger
Enter:

Bearer YOUR_TOKEN

Then test:

POST /items


🛡 Security Features
Password hashing using bcrypt

JWT access tokens

Protected routes

Token validation middleware

SQLAlchemy ORM (prevents raw SQL injection)


🧪 Security Testing
You can test this API using:
Postman
OWASP ZAP
Burp Suite


Test for:
Broken Authentication
SQL Injection
IDOR
JWT manipulation
Missing Authorization


📌 Future Improvements
 Move SECRET_KEY to .env
 Add Refresh Tokens
 Role-Based Access Control (Admin only endpoints)
 Rate Limiting
 Docker Support
 Logging & Monitoring
 PostgreSQL Support
 CI/CD Integration
 

📊 Learning Objectives
This project demonstrates:
REST API Development
Authentication & Authorization
Secure Password Storage

Backend Architecture

Application Security Basics




👨‍💻 Author

Theodore
Backend Developer | ERP Developer | Future Application Security Engineer
