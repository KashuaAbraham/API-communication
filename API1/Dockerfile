# Dockerfile for API-1
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install Flask
RUN pip install flask

# Expose port 5001
EXPOSE 5001

# Define the command to run the application
CMD ["python", "api1.py"]
