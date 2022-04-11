import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking')
from dbConnection import getData, closeConnection

def getUpcomingAppointments(cnx, identity):
    print("Displaying upcoming appointments")
    query = "SELECT * FROM doctorAppointments WHERE doctorId = " + str(identity) + " AND appointmenttime >= CURRENT_TIMESTAMP ORDER BY appointmenttime"
    data = getData(cnx, query)
    for i in range(len(data)):
        print("DoctorId:", data[i][0])
        print("PatientId:", data[i][1])
        print("Appointment Time:", data[i][2])
        print("\n")
    return

def getPreviousAppointments(cnx, identity):
    print("Displaying previous appointments")
    query = "SELECT * FROM doctorAppointments WHERE doctorId = " + str(identity) + " AND appointmenttime < CURRENT_TIMESTAMP ORDER BY appointmenttime DESC"
    data = getData(cnx, query)
    for i in range(len(data)):
        print("DoctorId:", data[i][0])
        print("PatientId:", data[i][1])
        print("Appointment Time:", data[i][2])
        print("\n")
    closeConnection(cnx)
    return

def getUpcomingAppointmentsWithPatient(cnx, identity, patientId):
    print("Displaying upcoming appointments")
    query = "SELECT * from doctorAppointments WHERE doctorID = " + str(identity) + " AND patientID = " + str(patientId) + " AND appointmenttime >= CURRENT_TIMESTAMP ORDER BY appointmenttime;"
    data = getData(cnx, query)
    data = getData(cnx, query)
    for i in range(len(data)):
        print("DoctorId:", data[i][0])
        print("PatientId:", data[i][1])
        print("Appointment Time:", data[i][2])
        print("\n")
    return

def getPreviousAppointmentsWithPatient(cnx, identity, patientId):
    print("Displaying previous appointments")
    query = "SELECT * from doctorAppointments WHERE doctorID = " + str(identity) + " AND patientID = " + str(patientId) + " AND appointmenttime < CURRENT_TIMESTAMP ORDER BY appointmenttime DESC;"
    data = getData(cnx, query)
    for i in range(len(data)):
        print("DoctorId:", data[i][0])
        print("PatientId:", data[i][1])
        print("Appointment Time:", data[i][2])
        print("\n")
    closeConnection(cnx)
    return