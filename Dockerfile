# Chronos Engine Dockerfile
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    xvfb libfaketime wget gnupg2 sqlite3 unzip \
    libxi6 libgconf-2-4 libnss3 libatk1.0-0 libatspi0 libx11-xcb1 \
    libxcb-dri3-0 libdrm2 libgbm1 libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV DISPLAY=:99
ENV FAKETIME_NO_CACHE=1

RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

# Install system dependencies
RUN apt-get update && apt-get install -y \
	xvfb libfaketime wget gnupg2 sqlite3 unzip \
	libxi6 libgconf-2-4 libnss3 libatk1.0-0 libatspi0 libx11-xcb1 \
	libxcb-dri3-0 libdrm2 libgbm1 libasound2 \
	&& rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
	&& apt-get update && apt-get install -y google-chrome-stable

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV DISPLAY=:99
ENV FAKETIME_NO_CACHE=1

RUN chmod +x entrypoint.sh
>>>>>>> c8dd0d8 (CHRONOS V2026: Core Initialization - Level 9 Modules Active)
ENTRYPOINT ["/app/entrypoint.sh"]
