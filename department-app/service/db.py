import mysql.connector


class DataBase:
    """Class to work with database."""
    def __init__(self, user, password, host, database):
        self.db = mysql.connector.connect(user=user,
                                          password=password,
                                          host=host,
                                          database=database)
        self.cursor = self.db.cursor()
        for i in open('./sql/create_tables.sql', 'r').read().split(';'):
            self.cursor.execute(i)

    def create_employee(self, name, department, salary, birth):
        """Insert new employee into table."""
        self.cursor.execute('INSERT INTO employee(Name, Department, Birth, Salary) VALUE (%s, %s, %s, %i)',
                            (name, department, birth, salary))

    def create_department(self, name):
        """Insert new department into table."""
        self.cursor.execute('INSERT INTO department VALUE (%s)', (name,))

    def remove_employee(self, id):
        """Remove employee from table."""
        self.cursor.execute('DELETE FROM employee WHERE id=%i', (id,))

    def remove_department(self, name):
        """Remove department from table."""
        self.cursor.execute('DELETE FROM department WHERE Name=%s', (name,))

    def edit_employee(self, id, new_name, new_birth, new_salary, new_department):
        """Edit data of employee."""
        pass

    def edit_department(self, name, new_name):
        """Change department name."""
        pass

    def get_employee(self, id):
        """Return employee data."""
        self.cursor.execute('SELECT * FROM employee WHERE id=%s', (id,))
        return self.cursor.fetchone()

    def get_department(self, name):
        """Return department data."""
        self.cursor.execute('SELECT * FROM department WHERE Name=%s', (name,))
        return self.cursor.fetchone()[0]

    def get_employees(self):
        """Return employees data."""
        self.cursor.execute('SELECT * FROM employee')
        return self.cursor.fetchall()

    def get_departments(self):
        """Return department data"""
        self.cursor.execute('SELECT * FROM department')
        return self.cursor.fetchall()

    def close(self):
        """Save changes and close database."""
        self.db.commit()
        self.db.close()


# db = mysql.connector.connect(user='debian-sys-maint',
#                                     password='PggWbsvEVgDZUYar',
#                                     host='127.0.0.1',
#                                     database='roma')
