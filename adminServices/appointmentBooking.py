import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking')
from dbConnection import executeQuery, getData, closeConnection
from datetime import *

def appointmentBooking(cnx):
    patientId = int(input("Enter the patient Id: "))
    query = "SELECT * FROM doctors";
    doctors = getData(cnx, query)
    for i in range(len(doctors)):
        print(str(i+1) + ". Dr. " + doctors[i][1] + "(" + doctors[i][3] + ")")
    index = int(input("Enter the choice: ")) - 1
    doctorId = doctors[index][0]
    query = "SELECT hour(appointmenttime) FROM appointments WHERE doctorId = " + str(doctorId) + " and date(appointmenttime) = CURRENT_DATE;"
    bookedSlots = getData(cnx, query)
    shiftStartTime = int(str(doctors[index][4]).split(":")[0])
    shiftEndTime = int(str(doctors[index][5]).split(":")[0])
    done = False
    for i in range(max(shiftStartTime, datetime.now().hour+1), shiftEndTime):
        if i not in bookedSlots:
            appointmentTime = i
            done = True
            break
    if not done:
        print("No slots available for today")
        return
    query = "INSERT INTO appointments (doctorID, patientID, appointmenttime, appointmentUpdatedCount) VALUES (" + str(doctorId) + ", " + str(patientId) + ", '" + datetime.now().strftime('%Y-%m-%d') + " " + str(appointmentTime) + ":00:00.000000', 0)"
    print("Appointment fixed at " +  datetime.now().strftime('%Y-%m-%d') + " " + str(appointmentTime) + ":00:00")
    executeQuery(cnx, query)
    closeConnection(cnx)