FROM python:3.13.0a5-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Copy files from the Dockerfile directory to current directory inside Docker container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Add the current directory contents into the container at /app
COPY . .

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 for the Flask app to run on
EXPOSE 5000

# Run the command to start the app
CMD ["flask", "run"]