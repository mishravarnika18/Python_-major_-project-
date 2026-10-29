import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector
def setup_database():
    conn=mysql.connector.connect(host="localhost",user="root",password=os.getenv("DB_PASSWORD"))
    cursor=conn.cursor()
    cursor.execute("create database if not exists employees ")
    cursor.execute("use employees")
    cursor.execute("create table if not exists employee_details(Employee_ID int AUTO_INCREMENT PRIMARY KEY,Name varchar(50) not null,Department varchar(50) not null,Email varchar(60) not null)")
    cursor.execute("create table if not exists user_attendence(attendence_id int primary key AUTO_INCREMENT,Employee_ID int not null,att_date varchar(50) not null,attendance_status varchar(50) not null,unique key unique_employee_att(Employee_ID,att_date),foreign key (Employee_ID) references employee_details(Employee_ID))")
    cursor.execute("create table if not exists emp_salary(Salary_id int primary key AUTO_INCREMENT,Employee_ID int not null,salary_amount int not null,salary_month varchar(50) not null,salary_status varchar(50) not null,salaryyear int not null,unique key unique_employee_month(Employee_ID,salary_month,salaryyear),foreign key (Employee_ID) references employee_details(Employee_ID))")
    conn.commit()
    conn.close()
def connect_db():
    conn=mysql.connector.connect(host="localhost",user="root",password=os.getenv("DB_PASSWORD"),database="employees")
    return conn
    cursor=conn.cursor()
if __name__=="__menu__":
    connect_db
setup_database()