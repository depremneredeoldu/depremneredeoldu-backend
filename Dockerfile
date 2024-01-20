FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--port", "8080"]