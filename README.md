#  House Broker Flask App (Dockerized)

A **Dockerized House Broker web application** built using Flask and SQLAlchemy.  
This project allows users to **add, view, and manage property listings** with a simple and clean UI.

---

##  Features

- 🏡 Add new house listings  
- 📋 View all available properties  
- 💰 Display price, location, and description  
- 🐳 Fully Dockerized for easy deployment  
- ⚡ Lightweight (SQLite database, no setup needed)

---

##  Tech Stack

- **Backend:** Flask (Python)  
- **Database:** SQLite + SQLAlchemy  
- **Frontend:** HTML, Bootstrap  
- **Deployment:** Docker, Docker Compose  

---

##  Project Structure

```
house-broker/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│
├── config.py
├── run.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .dockerignore
```

---

##  Installation & Setup

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 🔹 2. Run with Docker

```bash
docker-compose up --build
```

---

### 🔹 3. Open in Browser

```
http://localhost:5000
```

---

## 🧪 Without Docker (Optional)

```bash
pip install -r requirements.txt
python run.py
```

---



## 🎯 Use Case

This project is ideal for:
- Beginners learning Flask  
- DevOps learners practicing Docker  
- Resume projects for freshers  

---

## 🚀 Future Improvements

- 🔐 User Authentication (Login/Register)  
- 🖼️ Image Upload for Houses  
- 🔍 Search & Filter Functionality  
- 🗄️ MySQL/PostgreSQL Integration  
- ☁️ AWS Deployment (EC2 + Nginx)  

---

## 🤝 Contributing

Feel free to fork this repo and improve it!

---



---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
