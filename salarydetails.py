from datetime import date
from databaseconnect import connect_db
import _mysql_connector
def add_salary():
    conn=connect_db()
    cursor=conn.cursor()
    while True:
        print("------------------------------------------")
        print("1.Add new salary details")
        print("2.Exit")
        try:
            choice=int(input("Enter input: "))
        except ValueError:
            print("Invalid Input")
            continue
        if choice==1:
            emp_id=int(input("Enter Employee ID: "))
            amount=int(input("Enter Monthly Salary: "))
            year=date.today().year
            print("Choose month of salary")
            print("1.January")
            print("2.February")
            print("3.March")
            print("4.April")
            print("5.May")
            print("6.June")
            print("7.July")
            print("8.August")
            print("9.September")
            print("10.October")
            print("11.November")
            print("12.December")
            try:
                month=int(input("Enter input: "))
            except ValueError:
                print("Invalid input")
                continue
            if month==1:
                s_month="January"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                else:
                    print("Invalid Input")
            elif month==2:
                s_month="February"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
            elif month==3:
                s_month="March"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                else:
                    print("Invalid Input")
            elif month==4:
                s_month="April"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                else:
                    print("Invalid Input")
            elif month==5:
                s_month="May"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                else:
                    print("Invalid Input")
            elif month==6:
                s_month="June"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                else:
                    print("Invalid Input")
            elif month==7:
                s_month="July"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                else:
                    print("Invalid Input")
            elif month==8:
                s_month="August"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                else:
                    print("Invalid Input")
            elif month==9:
                s_month="September"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                else:
                    print("Invalid Input")
            elif month==10:
                s_month="October"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                else:
                    print("Invalid Input")
            elif month==11:
                s_month="November"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    s_status="Salary credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
            elif month==12:
                s_month="December"
                print("Salary Status")
                print("1.Salary credited")
                print("2.Salary not credited")
                try:
                    status=int(input("Enter input: "))
                except ValueError:
                    print("Invalid input")
                    continue
                if status==1:
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                elif status==2:
                    s_status="Salary not credited"
                    cursor.execute("select*from employee_details where Employee_ID=%s",(emp_id,))
                    if cursor.fetchall():
                        cursor.execute("select* from emp_salary where Employee_ID=%s and salary_month=%s and salaryyear=%s",(emp_id,s_month,year))
                        if not cursor.fetchall():
                            cursor.execute("""insert into emp_salary(Employee_Id,salary_amount,salary_month,salary_status,salaryyear)
                    values(%s,%s,%s,%s,%s)""",(emp_id,amount,s_month,s_status,year))
                            conn.commit()
                            print("details added successfully")
                        else:
                            print("details already exist")
                    else:
                        print("Employee Id doesn't exist in database")
                else:
                    print("Invalid Input")
        elif choice==2:
            break
        else:
            print("Invalid Input")
def view_salary():
    conn=connect_db()
    cursor=conn.cursor()
    while True:
        print("------------------------------------------")
        print("1.View all salary data")
        print("2.View salary data by employee id")
        print("3.View salary data by month")
        print("4.Exit")
        try:
            choice=int(input("Enter Input: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice==1:
            cursor.execute("select* from emp_salary")
            if cursor.fetchall():
                cursor.execute("select* from emp_salary")
                rows=cursor.fetchall()
                for row in rows:
                    print(row)
            else:
                print("no data found")
        elif choice==2:
            try:
                emp_id=int(input("Enter Employee_ID: "))
            except ValueError:
                print("Invalid Input")
                continue
            cursor.execute("select* from emp_salary where Employee_ID=%s",(emp_id,))
            if cursor.fetchall():
                cursor.execute("select* from emp_salary where Employee_ID=%s",(emp_id,))
                rows=cursor.fetchall()
                for row in rows:
                    print(row)
            else:
                ("No matching record found")
        elif choice==3:
            print("Choose month of salary")
            print("1.January")
            print("2.February")
            print("3.March")
            print("4.April")
            print("5.May")
            print("6.June")
            print("7.July")
            print("8.August")
            print("9.September")
            print("10.October")
            print("11.November")
            print("12.December")
            try:
             month=int(input("Enter input: "))
            except ValueError:
                print("Invalid input")
                continue
            if month==1:
                months="January"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==2:
                months="February"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==3:
                months="March"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==4:
                months="April"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==5:
                months="May"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==6:
                months="June"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==7:
                months="July"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==8:
                months="August"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==9:
                months="September"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==10:
                months="October"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==11:
                months="November"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
            elif month==12:
                months="December"
                cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                if cursor.fetchall():
                    cursor.execute("select* from emp_salary where salary_month=%s",(months,))
                    rows=cursor.fetchall()
                    for row in rows:
                        print(row)
                else:
                    ("No matching record found")
        elif choice==4:
            break
        else:
            print("Invalid Value")
def smenu():
    while True:
        print("------------------------------------------")
        print("1.Add Salary Detail")
        print("2.View Salary Details")
        print("3.Exit")
        try:
            choice=int(input("Enter Input: "))
        except ValueError:
            print("Invalid input")
            continue
        if choice==1:
            add_salary()
        elif choice==2:
            view_salary()
        elif choice==3:
            break
        else:
            print("invalid input")
if __name__=="__main__":
    smenu()