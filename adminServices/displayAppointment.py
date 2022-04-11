import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking')
from dbConnection import getData, closeConnection

def getAllAppointments(cnx):
    query = "SELECT * FROM doctorAppointments ORDER BY appointmenttime"
    data = getData(cnx, query)
    for i in range(len(data)):
        print("DoctorId:", data[i][0])
        print("PatientId:", data[i][1])
        print("Appointment Time:", data[i][2])
        print("\n")
    return
