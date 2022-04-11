import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/utilities')
from dbConnection import getConnection
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/adminServices')
from patientRegisteration import patientRegisteration
from displayAppointment import getAllAppointments
from appointmentBooking import appointmentBooking
from updateAppointment import updateAppointment
from deleteAppointment import deleteAppointment
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking')
from dbConnection import executeQuery, getData, closeConnection

def getAdminMenu():
    print("1. Patient Registeration")
    print("2. Appointment Booking")
    print("3. Display all appointments")
    print("4. Update appointment")
    print("5. Delete appointment")
    print("6. Exit")
    return 6

def getRootCreds():
    return { "user": "root", "password": "" }

def getCnx():
    creds = getRootCreds()
    return getConnection(creds['user'], creds['password'])

def serviceAdmin(choice, identity):
    if choice == 1:
        return patientRegisteration(getCnx())
    if choice == 2:
        return appointmentBooking(getCnx())
    if choice == 3:
        return getAllAppointments(getCnx())
    if choice == 4:
        return updateAppointment(getCnx())
    if choice == 5:
        return deleteAppointment(getCnx())