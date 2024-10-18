FROM python:3.11-bullseye

# Update package list and install dependencies
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev  && apt-get clean

# Verify SQLite version
RUN sqlite3 --version

WORKDIR /app

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
