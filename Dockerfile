# pull base image
FROM python:3.7

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN pip install --upgrade pip wheel setuptools

WORKDIR /app

#install dependenciess
COPY Pipfile  Pipfile.lock /app/

RUN pip install pipenv && pipenv install --system

# Copy Project

COPY . /app/


