FROM python:3.12.0-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy app files
COPY ./app /code/app

# Run the application
CMD ["fastapi", "run", "app/main.py", "--port", "80"]