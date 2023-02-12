# pull official base image
FROM python:3.10.7-slim-buster

# set work directory
WORKDIR /rates-api

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update

# copy project
COPY . /rates-api

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt