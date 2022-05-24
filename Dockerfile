FROM python:alpine3.7

WORKDIR /app
COPY src/requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
RUN mkdir -p data
VOLUME ["config", "data"]
EXPOSE 5000
CMD ["./server.py"]
