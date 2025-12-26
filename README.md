────୨ৎ──── PSU SPHERE ────୨ৎ────
˙⋆✮ A Django-based student organization management system 
for Palawan State University. 

── .✦ FEATURES .✦ ── 
˙⋆✮ Manage Colleges, Programs, Students, and Organizations
˙⋆✮ Track organization memberships
˙⋆✮ Faker script to generate initial test data
˙⋆✮ User-friendly Django Admin with search and filters

𐔌՞꜆.  ̫.꜀՞𐦯 AUTHORS
˙⋆✮ Marlon Murillo
˙⋆✮ Grace Ann Cornel 

## Setup Instructions

1. **Clone this repository:**
git clone https://github.com/yourusername/projectsite.git
cd projectsite

2. **Create `requirements.txt`**

This file should list your project's Python dependencies.

3. **Review Dockerfile for environment variable syntax:**

Make sure `ENV` declarations are in the format:
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

4. **Build your Docker image:**
docker build -t my-django-applatest .

5. **Run Docker containers with Docker Compose:**
docker-compose up

Your Django app will be accessible at [http://localhost:8000](http://localhost:8000).

## Common Docker Commands

- Run migrations inside the container:
docker-compose exec web python manage.py migrate

- Create a superuser:
docker-compose exec web python manage.py createsuperuser

- Collect static files for production:
docker-compose exec web python manage.py collectstatic --noinput

- Run tests:
docker-compose exec web python manage.py test


## Pushing Docker Image to Docker Hub

1. Login to Docker Hub:
docker login

2. Tag your image:
docker tag my-django-applatest yourusername/django-applatest:latest

3. Push image:
docker push yourusername/django-applatest:latest

## Deploying to Another Machine

1. Pull the image on the target computer:
docker pull yourusername/django-applatest:latest

2. Run using a `docker-compose.yml` referencing the image.

3. Run migrations and other setup commands as needed.