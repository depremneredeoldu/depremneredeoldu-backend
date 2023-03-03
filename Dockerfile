FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY .env /app/.env

COPY ./app /app/app

VOLUME /home/production/db/ /app/db

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]