FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY src/requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy source code and model
COPY src/ ./src/
COPY models/ ./models/

# Set working dir to src
WORKDIR /app/src

# Expose API port
EXPOSE 8000

# Run FastAPI app
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
