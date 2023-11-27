# Specify Python version
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required packages
RUN pip install Flask

# Make port 5002 available
EXPOSE 5002

# Run the application
CMD ["python", "ReturnService.py"]
