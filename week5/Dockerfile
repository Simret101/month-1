
FROM python:3.12.9

WORKDIR /app


COPY . /app/


RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /env


RUN /env/bin/pip install --upgrade pip
COPY requirements.txt /app/
RUN /env/bin/pip install -r requirements.txt


EXPOSE 8000


ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=your_project.settings


CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
