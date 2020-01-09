from flask import Flask
from flask_restful import Api
import rest.rest_app as ra

app = Flask(__name__)
api = Api(app)

api.add_resource(ra.Departments, '/rest/departments')
api.add_resource(ra.Department, '/rest/departments/<string:department_name>')
api.add_resource(ra.Employees, '/rest/employees')
api.add_resource(ra.Employee, '/rest/employees/<int:employee_id>')

if __name__ == '__main__':
    app.run(debug=True)
