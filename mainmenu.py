from attendancedetail import amenu
from employeedetail import emenu
from salarydetails import smenu
def mainmenu():
    while True:
        print("------------------------------------------")
        print("Main Menu")
        print("1.Manage Employee Details")
        print("2.Manage Employees Attendence")
        print("3.Manage Employees Salary")
        print("4.Exit")
        try :
            choice=int(input("Enter your choice: "))
        except ValueError:
            print("invalid input")
            continue
        if choice==1:
            emenu()
        elif choice==2:
            amenu()
        elif choice==3:
            smenu()
        elif choice==4:
            break
        else:
            print("Invalid Input")
if __name__=="__main__":
    mainmenu()
