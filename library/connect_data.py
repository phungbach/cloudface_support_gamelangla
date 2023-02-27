import mysql.connector

def getConnection():
    khaibao = mysql.connector.connect(host='localhost',
                                    user='root',
                                    passwd='root',
                                    database='cloudface_support')
    return khaibao
