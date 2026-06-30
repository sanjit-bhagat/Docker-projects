# Docker Portfolio Website

This is my first Docker project where I deployed a simple portfolio website using the Nginx Docker image.

## Technologies Used

- Docker
- Nginx
- HTML

## Project Structure

```
docker-portfolio-website/
│── index.html
└── README.md
```

## How to Run

1. Pull the Nginx image:

```bash
docker pull nginx
```

2. Run the container:

```bash
docker run -d --name portfolio-container -p 8080:80 -v $(pwd):/usr/share/nginx/html nginx
```

3. Open your browser:

```
http://localhost:8080
```

## Docker Commands Used

```bash
docker pull nginx
docker run
docker ps
docker stop
docker start
docker rm
```

## What I Learned

- Docker Images
- Docker Containers
- Port Mapping
- Volume Mounting
- Running a static website with Nginx

## Author

**Sanjit Bhagat**
