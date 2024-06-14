# Dockerfile for API-2
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install Flask and Requests
RUN pip install flask requests

# Expose port 5002
EXPOSE 5002

# Define the command to run the application
CMD ["python", "api2.py"]
