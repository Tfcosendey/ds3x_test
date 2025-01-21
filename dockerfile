# Use Python Alpine
FROM python:3.11-alpine

# Set environment variables to avoid buffering and set the working directory
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt /app/

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

CMD ["python", "src/main.py"]
