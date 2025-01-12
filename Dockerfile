# Use an official Python runtime for version 3.12
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to make Flask use production server
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]

