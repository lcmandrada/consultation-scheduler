import view
import re, threading, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

class loginLogic():
    def __init__(self, app, window, view, data):
        self.app = app
        self.window = window
        self.view = view
        self.data = data
        self.account = 'account'
        self.slot = 'slot'

    def tryLogin(self, email, password):
        # check error
        if not email or not password:
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'Incomplete information.')
        else:
            self.checkLogin(email, password)

    def checkLogin(self, email, password):
        table = self.data.getTable(self.account)

        # check error
        if not table:
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'No user yet.')
        # check table
        else:
            # iterate emails
            for entry in table:
                # check email
                if email == entry[3]:
                    # check password
                    if password == entry[4]:
                        uid = entry[0]
                        student = entry[1] + " " + entry[2]
                        
                        if uid == 1:
                            # to advisor
                            self.advisorWindow = QtWidgets.QWidget()
                            self.advisorView = view.advisorView()
                            self.advisorView.setupUi(self.app, self.advisorWindow, self.view, self.data, uid, email, self.window)
                            self.advisorWindow.show()
                        else:
                            # to student
                            self.studentWindow = QtWidgets.QWidget()
                            self.studentView = view.studentView()
                            self.studentView.setupUi(self.app, self.studentWindow, self.view, self.data, uid, student, self.window)
                            self.studentWindow.show()
                            
                        self.cleanSlot()
                        self.window.close()
                        break
                    else:
                        QtWidgets.QMessageBox.warning(self.window, 'Error', 'Incorrect password.')
                        return
            else:
                QtWidgets.QMessageBox.warning(self.window, 'Error', 'User does not exist.')

    def toRegister(self):
        # create register
        self.registerWindow = QtWidgets.QDialog()
        self.registerView = view.registerView()
        self.registerView.setupUi(self.app, self.registerWindow, self.view, self.data)
        self.registerWindow.show()
        
    def addAccount(self, first, last, email, password, confirm):
        # check username
        if not first or not last or not email or not password or not confirm:
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'Incomplete information.')
            return
        # check name
        if not re.match("^[a-zA-Z ]+$", first) or not re.match("^[a-zA-Z ]+$", last):
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'Invalid characters.')
            return
        # check email
        if not re.match("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+$", email):
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'Email format:\nhello@world.edu')
            return
        # check passwords
        elif password != confirm:
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'Passwords do not match.')
            return
        else:
            table = self.data.getTable(self.account)

            # add if empty table
            if not table:
                self.data.addAccount(first, last, email, password)
                QtWidgets.QMessageBox.warning(self.window, 'Alert', 'Successful.')
                self.window.close()
                return

            # iterate emails
            for entry in table:
                # check existing
                if email == entry[3]:
                    QtWidgets.QMessageBox.warning(self.window, 'Error', 'Email is already taken.')
                    return
            # add account
            else:
                self.data.addAccount(first, last, email, password)
                QtWidgets.QMessageBox.warning(self.window, 'Alert', 'Successful.')
                self.window.close()
                return
                
    def cleanSlot(self):
        table = self.data.getTable(self.slot)
        
        # delete past schedules
        if table:
            for entry in table:
                if datetime.strptime(entry[1], "%a %b %d %Y").date() < datetime.now().date():
                    self.data.deleteSlot(entry[0])
                
class slotLogic():
    def __init__(self, app, view, data):
        self.app = app
        self.view = view
        self.data = data
        
    def addSlot(self, advisorView, window, date, start, end, location, aid):
        start = int(start[0:2] + start[3:5])
        end = int(end[0:2] + end[3:5])
        table = self.data.joinSlot(date)
        
        # check error
        if not location:
            QtWidgets.QMessageBox.warning(window, 'Error', 'Incomplete information.')
        elif not re.match("^[a-zA-Z0-9 .-]+$", location):
            QtWidgets.QMessageBox.warning(window, 'Error', 'Invalid characters.')
        elif start > end:
            QtWidgets.QMessageBox.warning(window, 'Error', 'Start cannot be ahead of End.')
        else:
            # add slot if empty table
            if not table:
                self.data.addSlot(date, start, end, location, aid)
                QtWidgets.QMessageBox.warning(window, 'Alert', 'Successful.')
                window.close()
                advisorView.getToday()
                return
                
            # iterate slots
            for entry in table:
                # check overlapping
                if (start >= entry[1] and start < entry[2]) or (end > entry[1] and end <= entry[2]) or (entry[1] >= start and entry[1] < end) or (entry[2] > start and entry[2] <= end):
                    QtWidgets.QMessageBox.warning(window, 'Error', 'Slot overlaps with an existing slot.')
                    break
            # add slot
            else:
                self.data.addSlot(date, start, end, location, aid)
                QtWidgets.QMessageBox.warning(window, 'Alert', 'Successful.')
                window.close()
                advisorView.getToday()
                return

    def editSlot(self, advisorView, window, date, sid, start, end, location):
        start = int(start[0:2] + start[3:5])
        end = int(end[0:2] + end[3:5])
        table = self.data.joinSlot(date)
        
        # check error
        if not location:
            QtWidgets.QMessageBox.warning(window, 'Error', 'Incomplete information.')
        elif not re.match("^[a-zA-Z0-9 .-]+$", location):
            QtWidgets.QMessageBox.warning(window, 'Error', 'Invalid characters.')
        elif start > end:
            QtWidgets.QMessageBox.warning(window, 'Error', 'Start cannot be later than End.')
        else:
            # iterate slots
            for entry in table:
                # check overlapping
                if sid != entry[0] and ((start >= entry[1] and start < entry[2]) or (end > entry[1] and end <= entry[2]) or (entry[1] >= start and entry[1] < end) or (entry[2] > start and entry[2] <= end)):
                    QtWidgets.QMessageBox.warning(window, 'Error', 'Slot overlaps with an existing slot.')
                    break
                elif sid == entry[0] and (start == entry[1] and end == entry[2] and location == entry[3]):
                    QtWidgets.QMessageBox.warning(window, 'Error', 'No edit detected.')
                    break
            # edit slot
            else:
                self.data.editSlot(sid, start, end, location)
                QtWidgets.QMessageBox.warning(window, 'Alert', 'Successful.')
                window.close()
                advisorView.getToday()

    def deleteSlot(self, sid):
        self.data.deleteSlot(sid)
        
    def getSlot(self, studentWindow, window, sid, uid, student, course, title, info, studentView):
        # check error
        if not title or not info:
            QtWidgets.QMessageBox.warning(window, 'Error', 'Incomplete information.')
        elif not re.match("^[a-zA-Z0-9 .-]+$", title):
            QtWidgets.QMessageBox.warning(window, 'Error', 'Invalid characters.')
        else:
            # lock slot
            self.data.addLocked(sid, uid, student, course, title, info)
            QtWidgets.QMessageBox.warning(window, 'Alert', 'Successful.')
            window.close()
            studentView.getToday()
            
    def voidSlot(self, sid):
        self.data.deleteLocked(sid)

class notificationLogic():
    def __init__(self, app, view, data, advisor):
        self.app = app
        self.view = view
        self.data = data
        self.advisor = advisor
        self.sender = 'skedcon@gmail.com'
        
    def autoNotify(self):
        # auto notify every 0800
        self.t = threading.Timer(60.0, self.autoNotify)
        trigger = "1000"
        self.t.start()
        
        # send automatic notification
        if datetime.now().strftime("%H%M") == trigger:
            # daily schedule to advisor
            today = datetime.now().strftime("%a %b %-d %Y")
            table = self.data.todayAdvisor(today)
            
            subject = "Auto Notify: {}".format(today)
            body = ""
            if not table:
                body += "CONSULTATION SCHEDULER\n{}\nNo schedule for today".format(today)
            else:
                body += "CONSULTATION SCHEDULER\n{}\nSchedule for today".format(today)
                body += "\n\n//////////\n\n"
                for entry in table:
                    body += "ID: {}\n".format(entry[0])
                    if len(str(entry[1])) == 3:
                        body += "Start: 0{}\n".format(entry[1])
                    else:
                        body += "Start: {}\n".format(entry[1])
                    if len(str(entry[2])) == 3:
                        body += "End: 0{}\n".format(entry[2])
                    else:
                        body += "End: {}\n".format(entry[2])
                    body += "Location: {}\n\n".format(entry[3])
                    body += "Student: {}\n".format(entry[4])
                    body += "Course: {}\n".format(entry[5])
                    body += "Title: {}\n\n".format(entry[6])
                    body += "Info:\n{}".format(entry[7])
                    body += "\n\n//////////\n\n"
                    
            self.sendNotification(["{}".format(self.advisor)], subject, body)
            print ("Auto Nofify: Sent to advisor.")
            
            # daily schedule to students
            table = self.data.todayStudent(today)
            
            subject = "Auto Notify: {}".format(today)
            if table:
                for entry in table:
                    body = "CONSULTATION SCHEDULER\n{}\nSchedule for today".format(today)
                    body += "\n\n//////////\n\n"
                    body += "ID: {}\n".format(entry[0])
                    if len(str(entry[1])) == 3:
                        body += "Start: 0{}\n".format(entry[1])
                    else:
                        body += "Start: {}\n".format(entry[1])
                    if len(str(entry[2])) == 3:
                        body += "End: 0{}\n".format(entry[2])
                    else:
                        body += "End: {}\n".format(entry[2])
                    body += "Location: {}\n\n".format(entry[3])
                    body += "Course: {}\n".format(entry[4])
                    body += "Title: {}\n\n".format(entry[5])
                    body += "Info:\n{}".format(entry[6])
                    body += "\n\n//////////\n\n"
                    
                    self.sendNotification(["{}".format(entry[9])], subject, body)
                    print ("Auto Nofify: Sent to student.")
        # stop auto notify
        elif int(datetime.now().strftime("%H%M")) > int(trigger):
            self.t.cancel()
            print ("Auto Nofify: Stopped.")
            
    def sendNotify(self, window, subject, body):
        table = self.data.selectEmail()
        recipient = []
        
        # check error
        if not subject or not body:
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'Incomplete information.')
        else:
        # send notification
            if len(table) > 1:
                for entry in table:
                    if entry[0] > 1:
                        recipient.append(entry[1])
                
                table = self.data.selectAvailable()
                body += "\n\nCONSULTATION SCHEDULER\nAvailable schedules"
                body += "\n\n//////////\n\n"
                if not table:
                    body += "No available schedule yet."
                else:
                    for entry in table:
                        body += "ID: {}\n".format(entry[0])
                        body += "Date: {}\n".format(entry[1])
                        if len(str(entry[2])) == 3:
                            body += "Start: 0{}\n".format(entry[2])
                        else:
                            body += "Start: {}\n".format(entry[2])
                        if len(str(entry[3])) == 3:
                            body += "End: 0{}\n".format(entry[3])
                        else:
                            body += "End: {}\n".format(entry[3])
                        body += "Location: {}".format(entry[4])
                        body += "\n\n//////////\n\n"
                print ("Send Notify: Sending.")
                self.sendNotification(recipient, subject, body)
                print ("Send Notify: Sent.")
                QtWidgets.QMessageBox.warning(window, 'Alert', 'Successful.')
            else:
                QtWidgets.QMessageBox.warning(window, 'Error', 'No students yet.')
            window.close()
            
    def sendNotification(self, recipient, subject, body):
        # set mail parameters
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = ", ".join(recipient)
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # start connection and send
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.sender, "COE125B14Q1718")
        text = msg.as_string()
        server.sendmail(self.sender, recipient, text)
        server.quit
        
    def __del__(self):
        self.t.cancel()
