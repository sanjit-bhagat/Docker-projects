
FROM python:3.12-slim

WORKDIR /app

COPY Requirement.txt .

RUN pip install --no-cache-dir -r Requirement.txt

COPY . .

CMD ["python","app.py"]

