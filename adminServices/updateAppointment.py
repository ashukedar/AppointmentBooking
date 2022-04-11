import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking')
from dbConnection import executeQuery, getData, closeConnection
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/utilities')
from datetime import *

def updateAppointment(cnx):
    patientId = int(input("Enter the patient Id: "))
    query = "SELECT * FROM doctors";
    doctors = getData(cnx, query)
    for i in range(len(doctors)):
        print(str(i+1) + ". Dr. " + str(doctors[i][1]) + "(" + str(doctors[i][3]) + ")")
    index = int(input("Enter the choice: ")) - 1
    doctorId = doctors[index][0]
    query = "SELECT hour(appointmenttime) FROM appointments WHERE doctorID = " + str(doctorId) + " AND patientID = " + str(patientId) + " AND date(appointmenttime) = CURRENT_DATE"
    data = getData(cnx, query)
    if len(data) > 0:
        prevAppointmentTime = int(str(data[0][0]).split(":")[0])
    else:
        print("No appointment found for today")
        return
    query = "SELECT hour(appointmenttime) FROM appointments WHERE doctorId = " + str(doctorId) + " and date(appointmenttime) = CURRENT_DATE;"
    bookedSlots = getData(cnx, query)
    shiftStartTime = int(str(doctors[index][4]).split(":")[0])
    shiftEndTime = int(str(doctors[index][5]).split(":")[0])
    done = False
    for i in range(prevAppointmentTime+1, shiftEndTime):
        if i not in bookedSlots[0]:
            appointmentTime = i
            done = True
            break;
    if not done:
        print("No slots available for today")
        return
    query = "UPDATE appointments SET appointmenttime = '" + datetime.now().strftime('%Y-%m-%d') + " " + str(appointmentTime) + ":00:00.000000' WHERE patientID = " + str(patientId) + " AND doctorID = " + str(doctorId) + " AND date(appointmenttime) = CURRENT_DATE"
    executeQuery(cnx, query)
    print("New slot booked at " + datetime.now().strftime('%Y-%m-%d') + " " + str(appointmentTime) + ":00:00")
    closeConnection(cnx)
    return