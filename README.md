# Case Community Reliability
Case Community Reliability

# Comando Docker
docker-compose build
docker-compose up
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "django-admin startproject app ."

# Comando Docker Test
docker-compose run --rm app sh -c "python manage.py test"
docker-compose run --rm app sh -c "flake8"
