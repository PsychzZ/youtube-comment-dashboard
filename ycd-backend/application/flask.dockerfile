FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
COPY .env ./

COPY controller/ /controller/
RUN ls --recursive /app/

RUN chmod --recursive 777 /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH /app

COPY . .

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000" ]