FROM python:3.8-slim

WORKDIR /app

COPY ./app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD ["python", "main.py"]
