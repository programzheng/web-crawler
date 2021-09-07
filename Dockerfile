FROM python:3.7

RUN pip install python-dotenv fastapi uvicorn requests bs4

COPY ./app /app

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]