import mysql.connector


class DataBase:
    def __init__(self, user, password, host, database):
        self.db = mysql.connector.connect(user=user,
                                          password=password,
                                          host=host,
                                          database=database)
        self.cursor = self.db.cursor()
        for i in open('../sql/create_tables.sql', 'r').read().split(';'):
            self.cursor.execute(i)

    def create_employee(self, name, department, salary, birth):
        self.cursor.execute('INSERT INTO employee(Name, Department, Birth, Salary) VALUE ("%s", "%s", "%s", "%s")',
                            (name, department, birth, salary))

    def create_department(self, name):
        self.cursor.execute('INSERT INTO department VALUE ("%s")', (name,))

    def remove_employee(self, id):
        self.cursor.execute('DELETE FROM employee WHERE id=%s', (id,))

    def remove_department(self, name):
        self.cursor.execute('DELETE FROM department WHERE Name="%s"', (name,))

    def edit_employee(self, id, new_name='', new_birth='', new_salary='', new_department=''):
        pass

    def edit_department(self, name, new_name):
        pass

    def get_employee(self, id):
        self.cursor.execute('SELECT * FROM employee WHERE id=%s', (id,))
        return self.cursor.fetchone()[0]

    def get_department(self, name):
        self.cursor.execute('SELECT * FROM department WHERE Name="%s"', (name,))
        return self.cursor.fetchone()[0]

    def close(self):
        self.db.commit()
        self.db.close()


# db = mysql.connector.connect(user='debian-sys-maint',
#                                     password='PggWbsvEVgDZUYar',
#                                     host='127.0.0.1',
#                                     database='roma')
