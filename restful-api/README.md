# 🚀 RESTful API Examples

A comprehensive collection of Python REST API implementations demonstrating different approaches and security patterns.

## 📚 Overview
This project showcases various ways to build and secure REST APIs using Python, from basic HTTP servers to fully secured Flask applications.

## 🗂️ Files Structure

### 1. 📡 task_02_requests.py
External API Integration
- 🔍 Features:
  - Fetches data from JSONPlaceholder API
  - Handles HTTP responses
  - Processes JSON data
  - CSV file export
- 🛠️ Technologies: `requests`, `csv`
- 📝 Usage: `python3 task_02_requests.py`

### 2. 🌐 task_03_http_server.py
Basic HTTP Server
- 🔍 Endpoints:
  - `GET /` : Welcome message
  - `GET /data` : Sample JSON data
  - `GET /info` : API metadata
  - `GET /status` : Health check
- 🛠️ Technologies: `http.server`, `socketserver`
- 🔌 Port: 8000
- 📝 Usage: `python3 task_03_http_server.py`

### 3. 🛠️ task_04_flask.py
Flask API with User Management
- 🔍 Endpoints:
  - `GET /` : Welcome page
  - `GET /data` : Users list
  - `GET /status` : API status
  - `GET /users/<username>` : User details
  - `POST /add_user` : Create user
- 🛠️ Technologies: `Flask`
- 🔌 Port: 5000
- 📝 Usage: `python3 task_04_flask.py`

### 4. 🔒 task_05_basic_security.py
Secured API Implementation
- 🔑 Security Features:
  - Basic Authentication
  - JWT Authentication
  - Role-based Access Control
- 🔍 Endpoints:
  - `GET /basic-protected` : Basic Auth demo
  - `POST /login` : JWT token generation
  - `GET /jwt-protected` : JWT validation
  - `GET /admin-only` : Role restriction
- 🛠️ Technologies: `Flask`, `flask-httpauth`, `flask-jwt-extended`
- 📝 Usage: `python3 task_05_basic_security.py`

## 🔧 Installation

```bash
# Create and activate virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip3 install flask flask-httpauth flask-jwt-extended requests
```

## 🧪 Testing

### 📡 Basic Request Testing
```bash
# Test external API integration
python3 task_02_requests.py
```

### 🌐 HTTP Server Testing
```bash
# Start server
python3 task_03_http_server.py

# Test endpoints
curl http://localhost:8000/
curl http://localhost:8000/data
curl http://localhost:8000/status
```

### 🛠️ Flask API Testing
```bash
# Start server
python3 task_04_flask.py

# Test endpoints
curl http://localhost:5000/
curl http://localhost:5000/data
curl -X POST -H "Content-Type: application/json" \
     -d '{"username":"test_user"}' \
     http://localhost:5000/add_user
```

### 🔒 Security Testing
```bash
# Start secured server
python3 task_05_basic_security.py

# Test Basic Authentication
curl -u user1:password http://localhost:5000/basic-protected

# Get JWT Token
curl -X POST -H "Content-Type: application/json" \
     -d '{"username":"user1","password":"password"}' \
     http://localhost:5000/login

# Use JWT Token
export TOKEN="<your_token_here>"
curl -H "Authorization: Bearer $TOKEN" \
     http://localhost:5000/jwt-protected
```

## 📋 Requirements
- Python 3.8+
- Flask
- Requests
- Flask-HTTPAuth
- Flask-JWT-Extended

## 💡 Tips
- Keep the SECRET_KEY secure in production
- Use environment variables for sensitive data
- Test all endpoints thoroughly
- Monitor server logs for security issues


## 👤 Author
Patrick MICHEL
