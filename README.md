# Case Community Reliability
Case Community Reliability

# Comando Docker
docker-compose build
docker-compose up
docker-compose down
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose run --rm app sh -c "django-admin startapp core"

# Comando Docker Test
docker-compose run --rm app sh -c "python manage.py test"
docker-compose run --rm app sh -c "flake8"
