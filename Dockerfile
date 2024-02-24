# Use an official Python runtime as a parent image
FROM python:3.11.6

ENV PYTHONUNBUFFERED 1

# Create a new directory in container - django-project
RUN mkdir /django-project

# Set the working directory in the container
WORKDIR /django-project

# add in this directory files
ADD . /django-project/

# Install any needed dependencies specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Install mysqlclient
RUN pip install mysqlclient

# Copy the current directory contents into the container at /app
COPY . /django-project/

# Copy .env file from directory to the inside our container
COPY .env /django-project/.env