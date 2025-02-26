FROM python:3.9-slim

WORKDIR /app

COPY heartbeat.py .
COPY requirements_heartbeat.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "heartbeat.py"]
