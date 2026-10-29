import mysql.connector
from datetime import date
from databaseconnect import connect_db
def record_attendence():
    conn=connect_db()
    cursor=conn.cursor()
    while True:
        print("------------------------------------------")
        print("1.Record attendence")
        print("2.Exit")
        try:
            choice=int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Input")
            continue
        if choice==1:
            emp_id=int(input("Enter employee Id: "))
            cursor.execute("select 1 from employee_details where Employee_ID=%s",(emp_id,))
            if cursor.fetchone():
                at_date=date.today()
                print("1.Present")
                print("2.Absent")
                print("3.Leave")
                try:
                    Choices=int(input("Please enter value: "))
                except ValueError:
                    print("Invalid Input")
                    continue
                if Choices==1:
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchone():
                        cursor.execute("select*from user_attendence where Employee_ID=%s and att_date=%s",(emp_id,at_date,))
                        if not cursor.fetchall():
                            status="Present"
                            cursor.execute("""insert into user_attendence(Employee_ID,att_date,attendance_status)
                    values(%s,%s,%s)""",(emp_id,at_date,status))
                            conn.commit()
                            print("attendence successfully captured")
                        else:
                            print("attendence captured already")
                    else:
                        print("Employee Id doesn't exist in database.")
                elif Choices==2:
                    if cursor.fetchone():
                        cursor.execute("select*from user_attendence where Employee_ID=%s and att_date=%s",(emp_id,at_date,))
                        if not cursor.fetchall():
                            status="Absent"
                            cursor.execute("""insert into user_attendence(Employee_ID,att_date,attendance_status)
                    values(%s,%s,%s)""",(emp_id,at_date,status))
                            conn.commit()
                            print("attendence successfully captured")
                        else:
                            print("attendence captured already")
                    else:
                        print("Employee Id doesn't exist in database.")
                elif Choices==3:
                    if cursor.fetchone():
                        cursor.execute("select*from user_attendence where Employee_ID=%s and att_date=%s",(emp_id,at_date,))
                        if not cursor.fetchall():
                            status="Present"
                            cursor.execute("""insert into user_attendence(Employee_ID,att_date,attendance_status)
                    values(%s,%s,%s)""",(emp_id,at_date,status))
                            conn.commit()
                            print("attendence successfully captured")
                        else:
                            print("attendence captured already")
                    else:
                        print("Employee Id doesn't exist in database.")
                else:
                    print("Invalid input")
            else:
                print(f"Employee id {emp_id} does not exists")
        elif choice==2:
            break
        else:
            print("Invalid Input")
    conn.close()
def view_attendence():
    conn=connect_db()
    cursor=conn.cursor()
    while True:
        print("------------------------------------------")
        print("1.View all attendence")
        print("2.View attendence by emoloyee id")
        print("3.View attendance by date")
        print("4.View attendance by status")
        print("5.Exit")
        try:
            choice=int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Input")
            continue
        if choice==1:
            cursor.execute("select*from user_attendence")
            rows=cursor.fetchall()
            for row in rows:
                print(row)
        elif choice==2:
            try:
                emp_id=int(input("Enter employee id: "))
            except ValueError:
                print("Invalid Input")
                continue
            cursor.execute("select*from user_attendence where Employee_ID=%s",(emp_id,))
            if cursor.fetchall():
                cursor.execute("select*from user_attendence where Employee_ID=%s",(emp_id,))
                rows=cursor.fetchall()
                for row in rows:
                    print(rows)
            else:
                print("Employee Id not found")
        elif choice==3:
            Date=input("Enter Date in YYYY-MM-DD Format: ")

            cursor.execute("select*from user_attendence where att_date=%s",(Date,))
            if cursor.fetchall():
                cursor.execute("select*from user_attendence where att_date=%s",(Date,))
                rows=cursor.fetchall()
                for row in rows:
                    print(row)
            else:
                print("Employee Id not found")  
        elif choice==4:
            print("1.Present")
            print("2.Absent")
            print("3.Leave")
            try:
                Choices=int(input("Enter your choice: "))
            except ValueError:
                print("Invalid Input")
                continue
            if Choices==1:
                status="Present"
                cursor.execute("select*from user_attendence where attendance_status=%s",(status,))
                if cursor.fetchall():
                    cursor.execute("select*from user_attendence where attendance_status=%s",(status,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    print("Employee Id not found") 
            elif Choices==2:
                status="Absent"
                cursor.execute("select*from user_attendence where attendance_status=%s",(status,))
                if cursor.fetchall():
                    cursor.execute("select*from user_attendence where attendance_status=%s",(status,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    print("Employee Id not found") 
            elif Choices==3:
                status="Leave"
                cursor.execute("select*from user_attendence where attendance_status=%s",(status,))
                if cursor.fetchall():
                    cursor.execute("select*from user_attendence where attendance_status=%s",(status,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    print("Employee Id not found") 
        elif choice==5:
            break
        else:
            print("invalid input")
    conn.close()
def amenu():
    while True:
        print("------------------------------------------")
        print("1.Record Employee Attendence")
        print("2.View attendence")
        print("3.Exit")
        try:
            choice=int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Input")
            continue
        if choice==1:
            record_attendence()
        elif choice==2:
            view_attendence()
        elif choice==3:
            break
        else:
            print("Invalid Input")
if __name__=="__main__":
    amenu()