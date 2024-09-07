# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install any needed Python packages (if required)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Default command if no file is specified, but you'll typically override this at runtime
CMD ["python"]