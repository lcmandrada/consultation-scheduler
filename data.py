import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

class dataTools():
    def __init__(self, database):
        self.database = database

        # log in to database
        with open('.passwd', 'r') as f:
	        pw = f.read()
        self.session = mysql.connector.connect(user = 'root', password = pw, host = '127.0.0.1', autocommit = True)
        self.cursor = self.session.cursor()

        # connect to database
        self.connectDatabase()
        
        # create table
        self.createAccount()
        self.createSlot()
        self.createLocked()

    def connectDatabase(self):
        # set session database
        try:
            self.session.database = self.database
        except mysql.connector.Error as e:
            # create database if not existing
            if e.errno == errorcode.ER_BAD_DB_ERROR:
                self.createDatabase()
                self.session.database = self.database
            else:
                print("Error: {}".format(e.msg))

    def createDatabase(self):
        # create database
        try:
            self.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8';".format(self.database))
        except mysql.connector.Error as e:
            print("Error: {}".format(e.msg))

    def createAccount(self):
        # create table for account
        command = (" CREATE TABLE IF NOT EXISTS account ("
                    " `uid` int(5) NOT NULL AUTO_INCREMENT,"
                    " `first` char(50) NOT NULL,"
                    " `last` char(50) NOT NULL,"
                    " `email` char(50) NOT NULL,"
                    " `password` char(50) NOT NULL,"
                    " PRIMARY KEY (`uid`)"
                    ") ENGINE=InnoDB;")
        self.execute(command)

    def createSlot(self):
        # create table for slots
        command = (" CREATE TABLE IF NOT EXISTS slot ("
                    " `sid` int(5) NOT NULL AUTO_INCREMENT,"
                    " `date` char(50) NOT NULL,"
                    " `start` int(10) NOT NULL,"
                    " `end` int(10) NOT NULL,"
                    " `location` char(50) NOT NULL,"
                    " `aid` int(5) NOT NULL,"
                    " PRIMARY KEY (`sid`)"
                    ") ENGINE=InnoDB;")
        self.execute(command)

    def createLocked(self):
        # create table for taken
        command = (" CREATE TABLE IF NOT EXISTS locked ("
                    " `sid` int(5) NOT NULL,"
                    " `uid` int(5) NOT NULL,"
                    " `student` char(50) NOT NULL,"
                    " `course` char(50) NOT NULL,"
                    " `title` char(100) NOT NULL,"
                    " `info` char(150) NOT NULL,"
                    " PRIMARY KEY (`sid`)"
                    ") ENGINE=InnoDB;")
        self.execute(command)

    def getTable(self, table):
        return self.execute("SELECT * FROM {};".format(table))

    def execute(self, command):
        # execute database command
        try:
            self.cursor.execute(command)
        except mysql.connector.Error as e:
            print("Error: {} with {}".format(e.msg, command))

        try:
            result = self.cursor.fetchall()
        except:
            result = self.cursor.fetchone()

        return result

    def addAccount(self, first, last, email, password):
        command = "INSERT INTO account (first, last, email, password) "
        command += "VALUES ('{}', '{}', '{}', '{}')".format(first, last, email, password)
        self.execute(command)
        
    def addSlot(self, date, start, end, location, aid):
        # add slot
        command = "INSERT INTO slot (date, start, end, location, aid) "
        command += "VALUES ('{}', '{}', '{}', '{}', '{}')".format(date, start, end, location, aid)
        self.execute(command)
        
    def addLocked(self, sid, uid, student, course, title, info):
        # add slot
        command = "INSERT INTO locked (sid, uid, student, course, title, info) "
        command += "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(sid, uid, student, course, title, info)
        self.execute(command)
        
    def joinSlot(self, date):
        command = "SELECT slot.sid, start, end, location, student, course, title, info "
        command += "FROM slot LEFT JOIN locked ON slot.sid = locked.sid WHERE date = '{}' ".format(date)
        command += "ORDER BY start;"
        return self.execute(command)
        
    def joinLocked(self, date, uid):
        command = "SELECT slot.sid, start, end, location, student "
        command += "FROM slot LEFT JOIN locked ON slot.sid = locked.sid "
        command += "WHERE date = '{}' AND (uid = {} OR uid IS NULL) ".format(date, uid)
        command += "ORDER BY start;"
        return self.execute(command)
        
    def todayAdvisor(self, date):
        command = "SELECT slot.sid, start, end, location, student, course, title, info "
        command += "FROM locked LEFT JOIN slot ON locked.sid = slot.sid WHERE date = '{}' ".format(date)
        command += "ORDER BY start;"
        return self.execute(command)
        
    def todayStudent(self, date):
        command = "SELECT * FROM ( "
        command += "SELECT slot.sid, start, end, location, course, title, info, uid "
        command += "FROM locked LEFT JOIN slot on locked.sid = slot.sid "
        command += "WHERE date = '{}' ) as x ".format(date)
        command += "LEFT JOIN ( "
        command += "SELECT DISTINCT locked.uid, email "
        command += "FROM locked LEFT JOIN account on locked.uid = account.uid "
        command += ") as y on x.uid = y.uid;"
        return self.execute(command)
        
    def editSlot(self, sid, start, end, location):
        command = "UPDATE slot SET start = {}, end = {}, location = '{}' WHERE sid = {};".format(start, end, location, sid)
        self.execute(command)
    
    def deleteSlot(self, sid):
        command = "DELETE FROM slot WHERE sid = {};".format(sid)
        self.execute(command)
        self.deleteLocked(sid)

    def deleteLocked(self, sid):
        command = "DELETE FROM locked WHERE sid = {};".format(sid)
        self.execute(command)
        
    def selectEmail(self):
        command = "SELECT uid, email FROM account;"
        return self.execute(command)
        
    def selectAvailable(self):
        command = "SELECT slot.sid, date, start, end, location, student FROM slot "
        command += "LEFT JOIN locked ON slot.sid = locked.sid WHERE student IS NULL;"
        return self.execute(command)

    def __del__(self):
        self.session.commit()
        self.cursor.close()
        self.session.close()
