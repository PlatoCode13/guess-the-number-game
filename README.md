# 🎮 Guess the Number – Flask Game with Docker & CI/CD

[![Build Status](https://github.com/PlatoCode13/guess-the-number-game/actions/workflows/docker-build.yml/badge.svg)](https://github.com/PlatoCode13/guess-the-number-game/actions)

A simple, containerized web game built with Python Flask. Users try to guess a number between 1 and 10. The app is fully Dockerized and uses GitHub Actions for CI/CD — showcasing modern DevOps practices in a beginner-friendly project.

---

## 🚀 Features

- 🔢 Number guessing web game (1–10)
- 🐍 Python Flask backend
- 🐳 Dockerized for easy deployment
- ⚙️ GitHub Actions CI workflow (syntax check + Docker build)
- 📂 Organized, clean project structure

---

## 🧱 Tech Stack

- **Python 3.9**
- **Flask**
- **Docker**
- **GitHub Actions**
- *(Future: Kubernetes / OpenShift / Minikube)*

---

## 🛠️ Setup & Usage

### 🔧 Run Locally

```bash
python -m venv venv
venv\Scripts\activate         # For Windows
# OR
source venv/bin/activate      # For Linux/macOS

pip install -r requirements.txt
python app.py

Visit [http://localhost:5000](http://localhost:5000) in your browser.

```
---

### 🐳 Run in Docker

```bash
docker build -t guess-game .
docker run -p 5000:5000 guess-game
Then open: http://localhost:5000
```
🧪 CI/CD via GitHub Actions
On every push to the main branch, GitHub Actions will:

Check out the code

Install Python + dependencies

Run a syntax check using compileall

Build the Docker image

📂 Workflow file: .github/workflows/docker-build.yml

🗂️ Project Structure
```bash

.
├── app.py                     # Flask app
├── Dockerfile                 # Docker build instructions
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html             # Web UI template
├── .github/
│   └── workflows/
│       └── docker-build.yml  # GitHub Actions CI pipeline
└── .gitignore

```
