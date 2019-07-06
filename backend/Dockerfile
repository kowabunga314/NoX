FROM python:3.7
MAINTAINER dylan
ADD . /Projects/N1/backend
WORKDIR /Projects/N1/backend
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD exec gunicorn backend.wsgi:application --bind localhost:8000 --workers 3