# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose port
EXPOSE 8080

# Start FastAPI with uvicorn on port 8080
CMD ["uvicorn", "run_api:app", "--host", "0.0.0.0", "--port", "8080"]
