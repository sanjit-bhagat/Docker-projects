# 🚀 Docker Day 1 Project – Custom Nginx Website

## 📌 Project Overview
This is my first Docker project where I deployed a simple HTML website using an Nginx container.

The goal of this project was to understand:
- Docker images
- Containers
- Port mapping
- Volume mounting

---

## 🛠️ Technologies Used
- Docker
- Nginx
- HTML

---

## 📂 Project Structure
my-website/
│── index.html

⚙️ Steps to Run This Project
1. Pull Nginx Image
docker pull nginx
2. Run Container
docker run -d -p 8080:80 \
--name my-site \
-v $(pwd):/usr/share/nginx/html \
nginx
3. Open in Browser
http://localhost:8080
