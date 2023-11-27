# Specify Python version
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install required packages
RUN pip install Flask

# Make port 5001 available
EXPOSE 5001

# Run the application
CMD ["python", "AdditionService.py"]
