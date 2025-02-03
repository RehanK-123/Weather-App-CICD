# Use an official Python runtime as a parent image
FROM python:3.12.2

# Set the working directory
WORKDIR /app/DOCKER_DJANGO

# Copy the current directory contents into the container
COPY . /app/DOCKER_DJANGO
COPY /app/. /app/DOCKER_DJANGO/app
COPY /DOCKER_DJANGO/.  /app/DOCKER_DJANGO/DOCKER_DJANGO
COPY requirements.txt /app/requirements.txt
# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]