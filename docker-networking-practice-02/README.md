# Docker Networking Practice

## 📌 Project Overview

This project demonstrates the basics of Docker Networking. It covers how containers communicate using Docker's built-in networks and custom bridge networks.

## 🎯 Objectives

- Understand Docker Networking
- Create custom Docker networks
- Connect multiple containers
- Inspect Docker networks
- Enable container-to-container communication


## 📂 Project Structure

```
docker-networking/
│── README.md
└── screenshots/
```

## Commands Used

### List Docker Networks

```bash
docker network ls
```

### Create a Custom Network

```bash
docker network create web-network
```

### Verify Network

```bash
docker network inspect web-network
```

### Run Frontend Container

```bash
docker run -dit --name frontend --network web-network nginx
```

### Run Backend Container

```bash
docker run -dit --name backend --network web-network ubuntu
```

### Access Backend Container

```bash
docker exec -it backend bash
```

### List Running Containers

```bash
docker ps
```

### Remove Containers

```bash
docker rm -f frontend backend
```

### Remove Network

```bash
docker network rm web-network
```

## Project Workflow

```
Create Custom Network
        │
        ▼
Run Frontend Container
        │
        ▼
Run Backend Container
        │
        ▼
Verify Network Connection
        │
        ▼
Inspect Network
        │
        ▼
Remove Containers & Network
```

## Learning Outcomes

- Learned Docker networking concepts.
- Created and managed custom bridge networks.
- Connected multiple containers to the same network.
- Inspected Docker networks.
- Practiced Docker networking commands.


## Author

**Sanjit Bhagat**
