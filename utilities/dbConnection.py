import mysql.connector

def getConnection(user, password):
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user=user,
        password=password,
        database="appointmentbooking")

def executeQuery(cnx, query):
    cur = cnx.cursor()
    cur.execute(query)
    return cur.lastrowid

def getData(cnx, query):
    cur = cnx.cursor()
    cur.execute(query)
    result = cur.fetchall()
    return result

def closeConnection(cnx):
    cnx.commit()
    cnx.close()