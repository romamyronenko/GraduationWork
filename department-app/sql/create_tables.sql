CREATE TABLE IF NOT EXISTS department(
    Name varchar(90) NOT NULL,
    UNIQUE (Name)
);
CREATE TABLE IF NOT EXISTS employee(
    id int auto_increment,
    Name varchar(90),
    Department varchar(90),
    Birth date,
    Salary int,
    PRIMARY KEY (id),
    FOREIGN KEY (Department) REFERENCES department(Name)
);