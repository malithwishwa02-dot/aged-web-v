# Dockerfile for cookies factory
# Use a Python 3.11 base with X11 support for headless GUI
FROM python:3.11-slim

# Install system dependencies for Chrome, Xvfb, and Anti-Detect libraries
RUN apt-get update && apt-get install -y \
	wget gnupg unzip xvfb libxi6 libgconf-2-4 \
	libnss3 libatk1.0-0 libatspi0 libx11-xcb1 \
	libxcb-dri3-0 libdrm2 libgbm1 libasound2 \
	libfaketime \
	&& rm -rf /var/lib/apt/lists/*

# Install Google Chrome (Stable)
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
	&& apt-get update && apt-get install -y google-chrome-stable

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application files
COPY . .

# Environment Variables for Headless Execution
ENV DISPLAY=:99
ENV PYTHONUNBUFFERED=1
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/faketime/libfaketime.so.1

# Entrypoint script: Starts Xvfb, sets display, and launches the production server
RUN echo "#!/bin/bash\nXvfb :99 -screen 0 1920x1080x24 &\nsource /app/.env 2>/dev/null || true\ngunicorn --worker-class gthread --threads 10 --workers 4 --bind 0.0.0.0:5000 flask_server:app" > /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 5000
ENTRYPOINT ["/app/entrypoint.sh"]
