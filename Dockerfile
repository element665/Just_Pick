# Build a cross-platform Python image
# Uses multi-platform support to work on amd64 and arm64 hosts
FROM python:3.12-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure logs flush straight to stdout
ENV PYTHONUNBUFFERED=1

WORKDIR /just_pick

# Copy application code
COPY . .

# Install dependencies first (better caching)
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "just_pick.py"]
