# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY app.py /app

# Install dependencies (Flask)
RUN pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
