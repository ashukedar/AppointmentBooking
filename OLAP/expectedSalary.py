from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd;

import sys
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/utilities')
from dbConnection import getConnection
sys.path.insert(0, 'C:/Users/Raider/Downloads/IIT ISM Dhanbad/Sem 2/courses/ADBMS/prac/Appointment booking/OLAP')
from getDataFrame import getDataFrame 
from getRegressorInfo import getRegressorInfo

def getRootCreds():
    return { "user": "root", "password": "" }

def getCnx():
    creds = getRootCreds()
    return getConnection(creds['user'], creds['password'])

def getExpectedSalary():
    cnx = getCnx()
    df1 = getDataFrame()
    x = df1.drop(['salary'], axis = 1)
    y = df1[['salary']]

    #Scaling feature
    x = StandardScaler().fit_transform(x)

    #Training Testing data split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)

    regressor = LinearRegression();
    regressor.fit(x_train, y_train)
    y_pred = regressor.predict(x_test)
    getRegressorInfo(regressor, x_test, y_test, y_pred)

#    expectedFee = int(input("Enter the expected fee charge from customer: "))
#    expectedWorkingHours = int(input("Enter the expected working hours per day: "))
#    expectedAvgMonthlyAppointments = int(input("Enter the expected monthly appointment count: "))
#    expectedSpecialization = input("Enter the expected specialization: ")

#   result = {
#       'fee': [expectedFee], 
#       'workingHours': [expectedWorkingHours], 
#        'avgMonthlyAppointments': [expectedAvgMonthlyAppointments],
#        expectedSpecialization: 1
#    }

#    print("Expected Salary:", regressor.predict(pd.DataFrame(result)))