# que_parezca_un_accidente

Install pipenv into the system https://github.com/kennethreitz/pipenv

$ pipenv install --three

$ pipenv shell -c

$ python manage.py migrate

$ python manage.py createsuperuser

$ python manage.py runserver

Add users here http://localhost:8000/admin/auth/user/


# actions

`/usr/bin/curl --data '{"state": "Visado"}' -X PATCH -H "Content-type: application/json" http://localhost:8000/issues/1/?token=bonita`
`/usr/bin/curl --data '{"type": "Auto"}' -X PATCH -H "Content-type: application/json" http://localhost:8000/issues/2/?token=bonita`
`/usr/bin/curl --data '{"monto": "1000"}' -X PATCH -H "Content-type: application/json" http://localhost:8000/issues/27/?token=bonita`

# to load some fixtures use the helpers

`python manage.py shell` then load the files inside the `%run helpers.py` and do `fixtures()`

