import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/adminServices')
from adminServices import serviceAdmin, getAdminMenu
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/OLAP')
from expectedSalary import getExpectedSalary
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/doctorServices')
from doctorServices import serviceDoctor, getDoctorMenu
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/patientServices')
from patientServices import servicePatient, getPatientMenu

while True:
    try:
        print("1. Admin")
        print("2. Doctor")
        print("3. Patient")
        print("4. Finance Manager")
        print("5. Exit")
        userType = int(input("Enter the user type: "))
        
        if userType == 1:
            getMenu = getAdminMenu
            identity = -1
            serviceUser = serviceAdmin
        elif userType == 2:
            identity = int(input("Enter your Id: "))
            getMenu = getDoctorMenu
            serviceUser = serviceDoctor
        elif userType == 3:
            identity = int(input("Enter your Id: "))
            getMenu = getPatientMenu
            serviceUser = servicePatient
        elif userType == 4:
            getExpectedSalary()
            continue
        elif userType == 5:
            break
        else:
            raise Exception()
        
        while True:
            try:
                print("\n\n***Menu***")
                menuItemCount = getMenu()
                choice = int(input("Enter the choice: "))
                if choice < 1 or choice > menuItemCount:
                    raise Exception()
                if choice == menuItemCount:
                    break
                serviceUser(choice, identity)
            except:
                print("Invalid input. Expected input: Integer between 1 to ", menuItemCount)
    except:
        print("Invalid input. Expected input: Integer between 1 to 5")