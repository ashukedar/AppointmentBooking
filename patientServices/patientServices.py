import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking')
from dbConnection import getConnection
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/patientServices')
from getAppointments import getPreviousAppointments, getUpcomingAppointments

def getPatientCreds():
    return { "user": "patientDbUser", "password": "Patient@123" }

def getCnx():
    creds = getPatientCreds()
    return getConnection(creds['user'], creds['password'])

def getPatientMenu():
    print("1. Display previous appointments")
    print("2. Display upcoming appointments")
    print("3. Exit")
    return 3

def servicePatient(choice, identity):
    if choice == 1:
        print("Display previous appointments")
        getPreviousAppointments(getCnx(), identity)
        return
    elif choice == 2:
        print("Display upcoming appointments")
        getUpcomingAppointments(getCnx(), identity)
        return