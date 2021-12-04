# maintenance
## A database web application for managing the maintenance of automobiles
### Usage
#### Create the database
`docker compose run web python manage.py migrate`
#### Create the first user
`docker compose run web python manage.py createsuperuser`
#### Run the web server
` docker compose up`
