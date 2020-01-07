from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from .. import service


app = Flask(__name__)
api = Api(app)


class Department(Resource):
    def get(self, department_name):
        pass

    def delete(self, department_name):
        pass

    def put(self, department_name):
        pass


class Departments(Resource):
    def get(self):
        pass

    def post(self):
        pass


class Employee(Resource):
    def get(self, employee_id):
        pass

    def delete(self, employee_id):
        pass

    def put(self, employee_id):
        pass


class Employees(Resource):
    def get(self):
        pass

    def post(self):
        pass


api.add_resource(Departments, '/departments')
api.add_resource(Departments, '/departments/<department_name>')
api.add_resource(Employees, '/employees')
api.add_resource(Employee, '/employees/<employee_id>')

if __name__ == '__main':
    app.run(debug=True)
