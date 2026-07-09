# 🐳 Dockerize Python Calculator

A simple Python Calculator application containerized using Docker. This project demonstrates how to create a Docker image, build it, and run a Python application inside a Docker container.

## 📁 Project Structure

```
dockerize-python-calculator/
│── Dockerfile
│── app.py
└── requirement.txt
```

## 🚀 Features

- Basic Python Calculator
- Dockerized using Dockerfile
- Lightweight Python base image
- Easy to build and run

## 🛠️ Technologies Used

- Python 3.7
- Docker

## 📄 Dockerfile

```dockerfile
FROM python:3.7-slim

WORKDIR /app

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY . .

CMD ["python", "app.py"]
```

## ⚙️ Build Docker Image

```bash
docker build -t python-calculator:v1 .
```

## ▶️ Run Container

```bash
docker run -it --name calculator python-calculator:v1
```

## 📋 Useful Docker Commands

```bash
docker images
docker ps -a
docker logs calculator
docker stop calculator
docker start -ai calculator
docker rm calculator
docker rmi python-calculator:v1
```

## 📚 Learning Objectives

- Understand Dockerfile instructions
- Build Docker images
- Run Docker containers
- Manage Docker images and containers
- Practice Docker basics

## 👨‍💻 Author

**Sanjit Bhagat**
