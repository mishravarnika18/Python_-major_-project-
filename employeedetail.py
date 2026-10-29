import mysql.connector
from databaseconnect import connect_db
def add_employee():
    conn=connect_db()
    cursor=conn.cursor()
    while True:
        print("------------------------------------------")
        print("1.Add new employee")
        print("2.Exit")
        try:
            choice=int(input("enter your input: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice==1:
            Name=input("Please enter Employee name: ")
            Department=input("Please enter Employee department name: ")
            Email=input("Please enter your Email address: ")
            query="""insert into employee_details(
            Name,Department,Email)
            values(%s,%s,%s)"""
            values=(Name,Department,Email)
            cursor.execute(query,values)
            conn.commit()
            print("new employee added successfully")
        elif choice==2:
            break
        else :
            print("Invalid input")
    conn.close()


def view_employee_data():
    conn=connect_db()
    cursor=conn.cursor()
    print("------------------------------------------")
    print("the data of employees is given below: ")
    cursor.execute("select* from employee_details")
    for row in cursor.fetchall():
        print(row)
    conn.close()
def search_employees():
    conn=connect_db()
    cursor=conn.cursor()
    while True:
        print("------------------------------------------")
        print("1.Search employee by employee id")
        print("2.Search employee by name")
        print("3.Exit")
        try:
            Choice=int(input("enter your input: "))
        except ValueError:
            print("Invalid input")
            continue
        if Choice==1:
            emp_id=int(input("Enter Employee ID: "))
            cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
            rows=cursor.fetchall()
        elif Choice==2:
            emp_name=input("Enter Employee name: ")
            cursor.execute("select*from employee_details where Name LIKE %s",(f"%{emp_name}%",))
            rows=cursor.fetchall()
        elif Choice==3:
            break
        else :
            print("Invalid input")
            continue
        cursor.close()
        if rows:
             for row in rows:
                print(row)
        else:
            print("Record not found")
def update_records():
    conn=connect_db()
    cursor=conn.cursor()
    while True:
        print("------------------------------------------")
        print("1.update employee name")
        print("2.update employee email")
        print("3.Exit")
        try:
            choice=int(input("enter your input: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice==1:
            emp_id=int(input("search data by employee id: "))
            cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
            rows=cursor.fetchone()
            conn.commit()
            print(rows)
            if not rows:
                print("no employee found with employee id: ",emp_id)
            else:
                newname=input("enter employee name: ")
                cursor.execute("update employee_details set Name=%s where Employee_ID=%s",(newname,emp_id))
                conn.commit()
                conn.close()
                print("details updated successfully")
        elif choice==2:
            emp_id=int(input("search data by employee id: "))
            cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
            rows=cursor.fetchone()
            conn.commit()
            print(rows)
            if not rows:
                print("no employee found with employee id: ",(emp_id,))
            else:
                newemail=input("enter employee email: ")
                cursor.execute("update employee_details set Email=%s where Employee_ID=%s",(newemail,emp_id))
                conn.commit()
                conn.close()
                print("details updated successfully")
        elif choice==3:
            break
        else:
            print("choose correct option")
def delete_records():
    conn=connect_db()
    cursor=conn.cursor()
    while True:
        print("------------------------------------------")
        print("1.Delete employee details by employee id")
        print("2.Exit")
        try:
            choice=int(input("enter your input: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice==1:
            emp_id=int(input("Enter employee id to delete: "))
            cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
            rows=cursor.fetchone()
            conn.commit()
            print(rows)
            if not rows:
                print("no employee found")           
            else:
                cursor.execute("delete from employee_details where Employee_ID=%s",(emp_id,))
                conn.commit()
                cursor.close()
                print("employee data deleted successfull")
        if choice==2:
            break
        else:
            print("Invalid input")
def emenu():
    while True:
        print("------------------------------------------")
        print("1.Add New Employee")
        print("2.View Employees Data")
        print("3.Search Employees")
        print("4.Update Employee details")
        print("5.Delete Employee Records")
        print("6.Exit")
        try:
            choice=int(input("Please enter input: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice==1:
            add_employee()
        elif choice==2:
            view_employee_data()
        elif choice==3:
            search_employees()
        elif choice==4:
            update_records()
        elif choice==5:
            delete_records()
        elif choice==6:
            break
        else:
            print("invalid input")
if __name__=="__main__":
    emenu()