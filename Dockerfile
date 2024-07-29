FROM python:3.9-slim

WORKDIR /kubernetes-redis

COPY requirements.txt /kubernetes-redis/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /kubernetes-redis

CMD ["python", "run.py"]