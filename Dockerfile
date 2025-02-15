FROM python:3.10

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy pyproject.toml and poetry.lock BEFORE installing dependencies
COPY pyproject.toml poetry.lock ./

# Configure Poetry (disable virtualenv) and install dependencies
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --only main

# Copy the rest of the application
COPY . .

# Expose the port
EXPOSE 8080

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app.main:app"]
