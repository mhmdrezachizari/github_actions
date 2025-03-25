# Use official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the port
EXPOSE 8000

# Run migrations and start server
CMD python manage.py migrate && python manage.py collectstatic --noinput && gunicorn app.wsgi:application --bind 0.0.0.0:8000
