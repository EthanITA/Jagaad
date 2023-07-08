# Dockerfile for Flask
FROM python:3.11

WORKDIR /be

ENV FLASK_ENV=production
ENV DATABASE_URL=postgresql://myuser:mypassword@db:5432/mydb
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:3000"]
