ARG VERSION_TAG=latest

FROM ubuntu:20.04

WORKDIR /app

COPY . .

RUN python3 -m pip install -e .

WORKDIR /app

EXPOSE 5000
EXPOSE 8080

CMD ["python3", "run_service.py"]