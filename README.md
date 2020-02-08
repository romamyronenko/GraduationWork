# GraduationWork
Clone project:

` git clone https://github.com/romamyronenko/GraduationWork `

goto path

`cd GratuationWork/`

`cd department-app/`

create envrionment 

`virtualenv py-env`

activate

`source py-env/bin/activate`

install modules

`pip install flask`

`pip install flask_restful`

`pip install mysql.connector`

`pip install gunicorn`

Run service
`gunicorn --bind 127.0.0.1:5000 wsgi:app`

Project work at host 127.0.0.1:5000
