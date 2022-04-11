from datetime import datetime
import pandas as pd

import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/utilities')
from dbConnection import getData, closeConnection
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/adminServices')
from adminServices import getCnx

def getDataFrame():
    cnx = getCnx()
    query = "SELECT doctorID, fee, TIMEDIFF(shiftEndTime, shiftStartTime), salary, specialization from doctors;"
    doctors = getData(cnx, query)

    query = "SELECT doctorID, COUNT(*) as monthlyFreq FROM doctorAppointments GROUP BY doctorID, year(appointmenttime), month(appointmenttime)"
    data = getData(cnx, query)
    result = {
        'fee': [], 
        'workingHours': [], 
        'avgMonthlyAppointments': [],
        'salary': [],
        'specialization': []
    }
    closeConnection(cnx)

    for i in range(len(doctors)):
        doctorId = doctors[i][0]
        temp = datetime.strptime(str(doctors[i][2]), '%H:%M:%S')
        workingHours = temp.hour + temp.minute/60
        total, count = 0, 0
        for j in range(len(data)):
            if data[j][0] == doctorId:
                count += 1
                total += data[j][1]
        if count == 0:
            avgMonthlyAppointments = 0
        else:
            avgMonthlyAppointments = total/count
        result['fee'].append(doctors[i][1])
        result['workingHours'].append(workingHours)
        result['avgMonthlyAppointments'].append(avgMonthlyAppointments)
        result['salary'].append(doctors[i][3])
        result['specialization'].append(doctors[i][4])

    df = pd.DataFrame(result)
    
    #Handle Categorical data
    df1 = pd.get_dummies(df.specialization)
    df1 = pd.concat([df, df1], axis = 'columns')
    df1 = df1.drop(['specialization', 'DA'], axis='columns')
    return df1