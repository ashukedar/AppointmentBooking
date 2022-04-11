import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking')
from dbConnection import executeQuery, closeConnection

def deleteAppointment(cnx):
    patientId = int(input("Enter the patient Id: "))
    doctorId = int(input("Enter the doctor Id: "))
    query = "DELETE FROM appointments WHERE patientID = " + str(patientId) + " and doctorID = " + str(doctorId);
    executeQuery(cnx, query)
    print("Appointment deleted successfully")
    closeConnection(cnx)
    return