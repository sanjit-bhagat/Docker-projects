# 📚 Library Management System using Docker

## Project Overview

This project is a simple **Library Management System** developed in Python and containerized using Docker. It demonstrates how to package a Python application into a Docker container so it can run consistently on any machine without installing Python locally.

## Features

* Add a new book
* Show available books
* Borrow a book
* Return a book
* Menu-driven interface
* Runs inside a Docker container

## Project Structure

```text
library-management/
│── app.py
│── Dockerfile
│── requirements.txt
│── .dockerignore
└── README.md
```

## Build the Docker Image

```bash
docker build -t library-management .
```

## Run the Docker Container

```bash
docker run -it library-management
```

## Technologies Used

* Python 3
* Docker

## Docker Concepts Practiced

* Dockerfile
* Docker Images
* Docker Containers
* Base Images
* Build Context
* Interactive Containers (`-it`)

## Learning Outcome

After completing this project, I learned how to containerize a Python application using Docker. I practiced creating a Dockerfile, building a Docker image, running containers, and understanding the Docker workflow for deploying Python applications.

## Author

**Sanjit Bhagat**

