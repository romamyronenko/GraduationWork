# GraduationWork
Clone project:

` git clone https://github.com/romamyronenko/GraduationWork `

goto path

`cd GratuationWork/`
`cd department-app/`

create envrionment 

`virtualenv py-env`
`source py-env/bin/activate`

`pip install flask`
`pip install flask_restful`
`pip install mysql.connector`
`pip install gunicorn`

Run service
`gunicorn --bind 0.0.0.0:5000 wsgi:app`

Project work at host 0.0.0.0:5000
