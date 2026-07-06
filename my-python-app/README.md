# 🐳 Dockerize a Python Calculator Application

## 📌 Project Overview

This project demonstrates how to containerize a simple Python Calculator application using Docker. The calculator runs in the terminal and performs basic arithmetic operations.

This project is created to practice Docker fundamentals such as creating a Dockerfile, building images, and running containers.

---

## 🚀 Features

* Addition
* Subtraction
* Multiplication
* Division
* Handles division by zero
* Runs inside a Docker container

---

## 📁 Project Structure

```text
docker-python-calculator/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3
* Docker

---

## ⚙️ Build the Docker Image

```bash
docker build -t python-calculator .
```

---

## ▶️ Run the Container

```bash
docker run -it python-calculator
```

---

## 📋 Example Output

```text
========== Python Calculator ==========

Enter First Number : 20
Enter Operator (+ - * /) : *
Enter Second Number : 5

Result = 100
```

---

## 📚 Docker Concepts Practiced

* Creating a Dockerfile
* Using a Python base image
* Working with `WORKDIR`
* Copying files using `COPY`
* Installing dependencies with `RUN`
* Running applications with `CMD`
* Building Docker images
* Running Docker containers

---

## 🎯 Learning Outcome

After completing this project, I learned how to package a Python application into a Docker container, build Docker images, run interactive containers, and understand the basic Docker workflow.

---

## 👨‍💻 Author

**Sanjit Bhagat**

