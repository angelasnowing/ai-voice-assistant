# FROM python:3.10.7
# ENV APP_HOME /app
# WORKDIR /app
# COPY . ./
# RUN pip install pipenv
# RUN pipenv install --deploy --system
# CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --threads 8 app.main:app
FROM python:3.10.7

ENV PYTHONUNBUFFERED 1
EXPOSE 8000
WORKDIR /app

COPY ./requirements.txt .

COPY ./ .

RUN pip install -r requirements.txt

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]