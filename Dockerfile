FROM python:3.12

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

COPY . .

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations



