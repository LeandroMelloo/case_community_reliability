# Case Community Reliability
Case Community Reliability

# Comando Docker
docker-compose build
docker-compose up
docker-compose down
docker volume rm case_community_reliability_dev-db-data
docker volume ls

# Comando Docker para criar um projeto Django e uma APP
docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose run --rm app sh -c "django-admin startapp core"

# Comando Docker Database
docker-compose run --rm app sh -c "python manage.py wait_for_db"
docker-compose run --rm app sh -c "python manage.py wait_for_db && flake8"
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py createsuperuser"

# Comando Docker Test
docker-compose run --rm app sh -c "python manage.py test"

# Comando Docker Lint
docker-compose run --rm app sh -c "flake8"
