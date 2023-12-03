FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app/app
COPY ./assets/lesserafim_logo.png /app/assets/