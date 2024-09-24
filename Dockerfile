# pull official base image
FROM python:3.11.4-slim-buster

# install dependencies
RUN pip install --upgrade pip
COPY ./locallibrary/requirements.txt .
RUN pip install -r requirements.txt

# copy project into container
copy ./locallibrary /app

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy entrypoint shell script to container
COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

EXPOSE 8000
