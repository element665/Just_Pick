FROM --platform=linux/amd64 python:3.11-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure logs flush straight to stdout
ENV PYTHONUNBUFFERED=1

WORKDIR /movie-slot

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

EXPOSE 5000

CMD ["python", "flask_app.py"]
