./wait-for-it.sh db:3306 -- flask db upgrade
gunicorn --bind 0.0.0.0:5000 app:app