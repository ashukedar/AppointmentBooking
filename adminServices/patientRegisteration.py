import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking')
from dbConnection import executeQuery, closeConnection

def setGender():
    while True:
        try:
            print("1. Male")
            print("2. Female")
            print("3. Other")
            option = int(input("Enter the number corresponding to gender: "))
            if option > 3 or option < 1:
                raise Exception()
            if option == 1:
                return 'Male'
            elif option == 2:
                return 'Female'
            elif option == 3:
                return 'Other'
        except:
            print("Invalid input. Expected input: Integer between 1 to 3")

def patientRegisteration(cnx):
    print("Patient Registeration")
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    gender = setGender();
    address = input("Enter the address: ")
    phoneNumber = input("Enter the phone number: ")
    query = "INSERT INTO patients(patientID, patientName, age, gender, address, phoneNumber) VALUES (null, '" + name + "', " + str(age) + ", '" + gender + "', '" + address + "', '" + phoneNumber + "')"
    newId = executeQuery(cnx, query)
    closeConnection(cnx)
    print("Patient registered successfully with id =", newId)
    return