import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking')
from dbConnection import getData, closeConnection

def getPreviousAppointments(cnx, identity):
    query = "SELECT * FROM appointments WHERE patientID = " + str(identity) + " and appointmenttime < CURRENT_TIMESTAMP ORDER BY appointmenttime DESC"
    data = getData(cnx, query)
    for i in range(len(data)):
        print("DoctorId:", data[i][0])
        print("PatientId:", data[i][1])
        print("Appointment Time:", data[i][2])
        print("\n")
    closeConnection(cnx)
    return

def getUpcomingAppointments(cnx, identity):
    query = "SELECT * FROM appointments WHERE patientID = " + str(identity) + " and appointmenttime >= CURRENT_TIMESTAMP ORDER BY appointmenttime DESC"
    data = getData(cnx, query)
    for i in range(len(data)):
        print("DoctorId:", data[i][0])
        print("PatientId:", data[i][1])
        print("Appointment Time:", data[i][2])
        print("\n")
    closeConnection(cnx)
    return
    