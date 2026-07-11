# 📦 Docker Volume - Persistent Storage

## 📖 Overview

This project demonstrates how to use **Docker Volumes** to store data permanently. The data remains available even after the container is removed.

## 🚀 Technologies Used

* Docker
* Ubuntu
* Linux

## 📂 Steps

### 1. Create a Docker Volume

```bash
docker volume create student-data
```

### 2. Run an Ubuntu Container

```bash
docker run -it --name student-app -v student-data:/notes ubuntu bash
```

### 3. Create a File

```bash
echo "Docker Volumes keep data safe." > /notes/student_notes.txt
```

### 4. Exit and Remove the Container

```bash
exit
docker rm student-app
```

### 5. Create a New Container Using the Same Volume

```bash
docker run -it --name student-app-new -v student-data:/notes ubuntu bash
```

### 6. Verify the Data

```bash
cat /notes/student_notes.txt
```

## 📌 Commands Used

```bash
docker volume create student-data
docker volume ls
docker volume inspect student-data
docker run -it --name student-app -v student-data:/notes ubuntu bash
docker rm student-app
```

## 🎯 Learning

* Create a Docker Volume
* Attach a volume to a container
* Store persistent data
* Reuse the same volume in another container
* Verify data persistence
