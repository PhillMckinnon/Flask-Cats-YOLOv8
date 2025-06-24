FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    git \
    gcc \
    g++ \
    libffi-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

RUN apt-get remove -y curl || true && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY app.py .
COPY fonts ./fonts
COPY model_folder/* ./model_folder/
COPY static ./static
COPY templates ./templates

EXPOSE 8080
CMD ["python3", "app.py"]