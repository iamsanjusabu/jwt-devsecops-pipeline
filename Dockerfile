FROM python:3.14.5

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

ENTRYPOINT ["fastapi", "run", "main.py"]
