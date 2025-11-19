FROM python:3.12.3-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app-backend.py templates/index.html ./

CMD ["python", "app-backend.py"]

