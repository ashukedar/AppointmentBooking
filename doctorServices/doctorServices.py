import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking')
from dbConnection import getConnection
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/doctorServices')
from displayAppointments import getUpcomingAppointments, getPreviousAppointments, getPreviousAppointmentsWithPatient, getUpcomingAppointmentsWithPatient

def getDoctorMenu():
    print("1. Display my appointments")
    print("2. Display appointments with specific patient")
    print("3. Exit")
    return 3

def getDoctorCreds():
    return { "user": "doctorDbUser", "password": "Doctor@456" }

def getCnx():
    creds = getDoctorCreds()
    return getConnection(creds['user'], creds['password'])

def serviceDoctor(choice, identity):
    if choice == 1:
        getUpcomingAppointments(getCnx(), identity)
        getPreviousAppointments(getCnx(), identity)
        return
    elif choice == 2:
        patientId = int(input("Enter the patient Id: "))
        getPreviousAppointmentsWithPatient(getCnx(), identity, patientId)
        getUpcomingAppointmentsWithPatient(getCnx(), identity, patientId)
        return