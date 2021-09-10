FROM python:3.7

RUN pip install python-dotenv fastapi uvicorn requests bs4

COPY ./app /app

ARG PORT
ENV PORT=$PORT
EXPOSE 80

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]