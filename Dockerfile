# 1. Use a Python version that matches pyproject.toml (>=3.13)
FROM python:3.13-slim

# Set environment variables for Python and uv
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PYTHONPATH=/app

# Set work directory
WORKDIR /app

# Install uv from its official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/

# Create a virtual environment
RUN uv venv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using a cache mount for speed.
# This layer is cached as long as pyproject.toml and uv.lock don't change.
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# Copy the rest of the application source code
# The '.' in the source path refers to the build context.
COPY . .

# Expose the port the app runs on
EXPOSE 8003

# Command to run the application in production using uvicorn.
# Assumes your FastAPI instance is named "app" in "app/main.py".
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8003"]
