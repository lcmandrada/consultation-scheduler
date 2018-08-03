'''
Consultation Scheduler
Luke Clark M. Andrada
'''

import sys, data, logic
from PyQt5 import QtCore, QtGui, QtWidgets

class loginView(object):
    def setupUi(self, app, loginWindow, view, data):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(321, 155)
        loginWindow.setFixedSize(321, 155)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(loginWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginGroup = QtWidgets.QGroupBox(loginWindow)
        self.loginGroup.setObjectName("loginGroup")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.loginGroup)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.userLayout = QtWidgets.QHBoxLayout()
        self.userLayout.setObjectName("userLayout")
        self.userLabel = QtWidgets.QLabel(self.loginGroup)
        self.userLabel.setObjectName("userLabel")
        self.userLayout.addWidget(self.userLabel)
        self.userLine = QtWidgets.QLineEdit(self.loginGroup)
        self.userLine.setObjectName("userLine")
        self.userLayout.addWidget(self.userLine)
        self.verticalLayout_3.addLayout(self.userLayout)
        self.passLayout = QtWidgets.QHBoxLayout()
        self.passLayout.setObjectName("passLayout")
        self.passLabel = QtWidgets.QLabel(self.loginGroup)
        self.passLabel.setObjectName("passLabel")
        self.passLayout.addWidget(self.passLabel)
        self.passLine = QtWidgets.QLineEdit(self.loginGroup)
        self.passLine.setInputMask("")
        self.passLine.setText("")
        self.passLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passLine.setObjectName("passLine")
        self.passLayout.addWidget(self.passLine)
        self.verticalLayout_3.addLayout(self.passLayout)
        self.actionLayout = QtWidgets.QHBoxLayout()
        self.actionLayout.setObjectName("actionLayout")
        self.loginButton = QtWidgets.QPushButton(self.loginGroup)
        self.loginButton.setObjectName("loginButton")
        self.actionLayout.addWidget(self.loginButton)
        self.addButton = QtWidgets.QPushButton(self.loginGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        self.addButton.setObjectName("addButton")
        self.actionLayout.addWidget(self.addButton)
        self.cancelButton = QtWidgets.QPushButton(self.loginGroup)
        self.cancelButton.setObjectName("cancelButton")
        self.actionLayout.addWidget(self.cancelButton)
        self.verticalLayout_3.addLayout(self.actionLayout)
        self.verticalLayout.addWidget(self.loginGroup)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

        # init
        view.centerWindow(loginWindow)
        self.loginLogic = logic.loginLogic(app, loginWindow, view, data)

        # connect buttons
        self.loginButton.clicked.connect(lambda: self.loginLogic.tryLogin(self.userLine.text(), self.passLine.text()))
        self.addButton.clicked.connect(lambda: self.loginLogic.toRegister())
        self.cancelButton.clicked.connect(lambda: loginWindow.close())

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "Login"))
        self.loginGroup.setTitle(_translate("loginWindow", "Login"))
        self.userLabel.setText(_translate("loginWindow", "Email"))
        self.passLabel.setText(_translate("loginWindow", "Password"))
        self.loginButton.setText(_translate("loginWindow", "Log In"))
        self.addButton.setText(_translate("loginWindow", "Register"))
        self.cancelButton.setText(_translate("loginWindow", "Cancel"))
        
class registerView(object):
    def setupUi(self, app, registerWindow, view, data):
        registerWindow.setObjectName("registerWindow")
        registerWindow.resize(505, 225)
        registerWindow.setFixedSize(505, 225)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(registerWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.registerGroup = QtWidgets.QGroupBox(registerWindow)
        self.registerGroup.setObjectName("registerGroup")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.registerGroup)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nameLayout = QtWidgets.QHBoxLayout()
        self.nameLayout.setObjectName("nameLayout")
        self.firstLabel = QtWidgets.QLabel(self.registerGroup)
        self.firstLabel.setObjectName("firstLabel")
        self.nameLayout.addWidget(self.firstLabel)
        self.firstLine = QtWidgets.QLineEdit(self.registerGroup)
        self.firstLine.setObjectName("firstLine")
        self.nameLayout.addWidget(self.firstLine)
        self.lastLabel = QtWidgets.QLabel(self.registerGroup)
        self.lastLabel.setObjectName("lastLabel")
        self.nameLayout.addWidget(self.lastLabel)
        self.lastLine = QtWidgets.QLineEdit(self.registerGroup)
        self.lastLine.setObjectName("lastLine")
        self.nameLayout.addWidget(self.lastLine)
        self.verticalLayout_3.addLayout(self.nameLayout)
        self.userLayout = QtWidgets.QHBoxLayout()
        self.userLayout.setObjectName("userLayout")
        self.userLabel = QtWidgets.QLabel(self.registerGroup)
        self.userLabel.setObjectName("userLabel")
        self.userLayout.addWidget(self.userLabel)
        self.userLine = QtWidgets.QLineEdit(self.registerGroup)
        self.userLine.setObjectName("userLine")
        self.userLayout.addWidget(self.userLine)
        self.verticalLayout_3.addLayout(self.userLayout)
        self.passLayout = QtWidgets.QHBoxLayout()
        self.passLayout.setObjectName("passLayout")
        self.passsLabel = QtWidgets.QLabel(self.registerGroup)
        self.passsLabel.setObjectName("passsLabel")
        self.passLayout.addWidget(self.passsLabel)
        self.passLine = QtWidgets.QLineEdit(self.registerGroup)
        self.passLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passLine.setObjectName("passLine")
        self.passLayout.addWidget(self.passLine)
        self.verticalLayout_3.addLayout(self.passLayout)
        self.confirmLayout = QtWidgets.QHBoxLayout()
        self.confirmLayout.setObjectName("confirmLayout")
        self.confirmLabel = QtWidgets.QLabel(self.registerGroup)
        self.confirmLabel.setObjectName("confirmLabel")
        self.confirmLayout.addWidget(self.confirmLabel)
        self.confirmLine = QtWidgets.QLineEdit(self.registerGroup)
        self.confirmLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmLine.setObjectName("confirmLine")
        self.confirmLayout.addWidget(self.confirmLine)
        self.verticalLayout_3.addLayout(self.confirmLayout)
        self.actionLayout = QtWidgets.QHBoxLayout()
        self.actionLayout.setObjectName("actionLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.actionLayout.addItem(spacerItem)
        self.addButton = QtWidgets.QPushButton(self.registerGroup)
        self.addButton.setObjectName("addButton")
        self.actionLayout.addWidget(self.addButton)
        self.cancelButton = QtWidgets.QPushButton(self.registerGroup)
        self.cancelButton.setObjectName("cancelButton")
        self.actionLayout.addWidget(self.cancelButton)
        self.verticalLayout_3.addLayout(self.actionLayout)
        self.verticalLayout.addWidget(self.registerGroup)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(registerWindow)
        QtCore.QMetaObject.connectSlotsByName(registerWindow)

        # init
        view.centerWindow(registerWindow)
        self.registerLogic = logic.loginLogic(app, registerWindow, view, data)
        
        # connect buttons
        self.addButton.clicked.connect(lambda: self.registerLogic.addAccount(self.firstLine.text(), self.lastLine.text(), self.userLine.text(), self.passLine.text(), self.confirmLine.text()))
        self.cancelButton.clicked.connect(lambda: registerWindow.close())
        
    def retranslateUi(self, registerWindow):
        _translate = QtCore.QCoreApplication.translate
        registerWindow.setWindowTitle(_translate("registerWindow", "Register"))
        self.registerGroup.setTitle(_translate("registerWindow", "Register"))
        self.firstLabel.setText(_translate("registerWindow", "First Name"))
        self.lastLabel.setText(_translate("registerWindow", "Last Name"))
        self.userLabel.setText(_translate("registerWindow", "Email"))
        self.passsLabel.setText(_translate("registerWindow", "Password"))
        self.confirmLabel.setText(_translate("registerWindow", "Confirm Password"))
        self.addButton.setText(_translate("registerWindow", "Register"))
        self.cancelButton.setText(_translate("registerWindow", "Cancel"))

class advisorView(object):
    def setupUi(self, app, advisorWindow, view, data, uid, advisor, loginWindow):
        advisorWindow.setObjectName("advisorWindow")
        advisorWindow.resize(903, 603)
        advisorWindow.setFixedSize(903, 603)
        self.viewGroup = QtWidgets.QGroupBox(advisorWindow)
        self.viewGroup.setGeometry(QtCore.QRect(10, 10, 881, 581))
        self.viewGroup.setFlat(False)
        self.viewGroup.setObjectName("viewGroup")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.viewGroup)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 881, 551))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.viewLayout = QtWidgets.QVBoxLayout()
        self.viewLayout.setObjectName("viewLayout")
        self.calendar = QtWidgets.QCalendarWidget(self.horizontalLayoutWidget)
        self.calendar.setAutoFillBackground(True)
        self.calendar.setGridVisible(False)
        self.calendar.setObjectName("calendar")
        self.viewLayout.addWidget(self.calendar)
        self.slotTree = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.slotTree.setAutoFillBackground(False)
        self.slotTree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.slotTree.setObjectName("slotTree")
        self.slotTree.headerItem().setText(0, "1")
        self.viewLayout.addWidget(self.slotTree)
        self.horizontalLayout.addLayout(self.viewLayout)
        self.actionLayout = QtWidgets.QVBoxLayout()
        self.actionLayout.setObjectName("actionLayout")
        self.calendarActions = QtWidgets.QVBoxLayout()
        self.calendarActions.setObjectName("calendarActions")
        self.addButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.calendarActions.addWidget(self.addButton)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.calendarActions.addWidget(self.line)
        self.notifyButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.notifyButton.setObjectName("notifyButton")
        self.calendarActions.addWidget(self.notifyButton)
        self.logoutButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.logoutButton.setObjectName("logoutButton")
        self.calendarActions.addWidget(self.logoutButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.calendarActions.addItem(spacerItem)
        self.actionLayout.addLayout(self.calendarActions)
        self.slotActions = QtWidgets.QVBoxLayout()
        self.slotActions.setObjectName("slotActions")
        self.editButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.editButton.setObjectName("editButton")
        self.slotActions.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.deleteButton.setObjectName("deleteButton")
        self.slotActions.addWidget(self.deleteButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.slotActions.addItem(spacerItem1)
        self.actionLayout.addLayout(self.slotActions)
        self.horizontalLayout.addLayout(self.actionLayout)
        self.viewGroup.raise_()
        self.editButton.raise_()

        self.retranslateUi(advisorWindow)
        QtCore.QMetaObject.connectSlotsByName(advisorWindow)
        
        # init
        view.centerWindow(advisorWindow)
        self.app = app
        self.window = advisorWindow
        self.view = view
        self.data = data
        self.uid = uid
        self.login = loginWindow
        self.slotLogic = logic.slotLogic(app, view, data)
        self.notificationLogic = logic.notificationLogic(app, view, data, advisor)
        
        # connect buttons
        self.calendar.clicked.connect(lambda: self.getToday())
        self.addButton.clicked.connect(lambda: self.toAdd())
        self.editButton.clicked.connect(lambda: self.toEdit())
        self.deleteButton.clicked.connect(lambda: self.toDelete())
        self.notifyButton.clicked.connect(lambda: self.toNotify())
        self.logoutButton.clicked.connect(lambda: self.logout())
        
        # initial events
        self.getToday()
        self.notificationLogic.autoNotify()

    def retranslateUi(self, advisorWindow):
        _translate = QtCore.QCoreApplication.translate
        advisorWindow.setWindowTitle(_translate("advisorWindow", "Advisor"))
        self.viewGroup.setTitle(_translate("advisorWindow", "View"))
        self.addButton.setText(_translate("advisorWindow", "Add Slot"))
        self.notifyButton.setText(_translate("advisorWindow", "Notify"))
        self.logoutButton.setText(_translate("advisorWindow", "Logout"))
        self.editButton.setText(_translate("advisorWindow", "Edit Slot"))
        self.deleteButton.setText(_translate("advisorWindow", "Delete Slot"))
        
    def getToday(self):
        self.date = self.calendar.selectedDate().toString()
        self.updateView()

    def updateView(self):
        # get data
        col = ["ID", "Start", "End", "Location", "Student", "Course", "Title", "Info"]
        table = self.data.joinSlot(self.date)

        # set headers
        for i, c in enumerate(col):
            self.slotTree.headerItem().setText(i, c)

        self.slotTree.clear()
        
        # populate table
        if table:
            for entry in range(len(table)):
                QtWidgets.QTreeWidgetItem(self.slotTree)
                for data in range(len(table[entry])):
                    if (data == 1 or data == 2) and len(str(table[entry][data])) == 3:
                        text = "0" + str(table[entry][data])
                        self.slotTree.topLevelItem(entry).setText(data, text)
                    else:
                        self.slotTree.topLevelItem(entry).setText(data, str(table[entry][data]))
                        
    def toAdd(self):
        # open add slot
        self.addWindow = QtWidgets.QDialog()
        self.addView = addView()
        self.addView.setupUi(self.addWindow, self.view, self.slotLogic, self.uid, self.date, self)
        self.addWindow.show()
        
    def toEdit(self):
        entry = self.slotTree.selectedItems()
        
        # check error
        if not entry:
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'No slot selected.')
        else:
            item = entry[0].text(0)
            sid = int(item)
            start = entry[0].text(1)
            end = entry[0].text(2)
            location = entry[0].text(3)
            
            # open edit slot
            self.editWindow = QtWidgets.QDialog()
            self.editView = editView()
            self.editView.setupUi(self.editWindow, self.view, self.slotLogic, self.date, sid, start, end, location, self)
            self.editWindow.show()
        
    def toDelete(self):
        entry = self.slotTree.selectedItems()
        
        # check error
        if not entry:
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'No slot selected.')
        else:
            item = entry[0].text(0)
            sid = int(item)

            reply = QtWidgets.QMessageBox.question(self.window, 'Confirm', 'Delete slot {}?'.format(sid), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            # delete slot
            if reply == QtWidgets.QMessageBox.Yes:
                self.slotLogic.deleteSlot(sid)
                QtWidgets.QMessageBox.warning(self.window, 'Alert', 'Successful.')
                self.getToday()
                
    def toNotify(self):
        # open notify
        self.notifyWindow = QtWidgets.QDialog()
        self.notifyView = notifyView()
        self.notifyView.setupUi(self.app, self.notifyWindow, self.view, self.data, self.notificationLogic)
        self.notifyWindow.show()
        
    def logout(self):
        # back to login
        self.window.close()
        self.login.show()
        
class addView(object):
    def setupUi(self, addWindow, view, logic, uid, date, advisorView):
        addWindow.setObjectName("addWindow")
        addWindow.resize(403, 163)
        addWindow.setFixedSize(403, 160)
        self.addGroup = QtWidgets.QGroupBox(addWindow)
        self.addGroup.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.addGroup.setFocusPolicy(QtCore.Qt.NoFocus)
        self.addGroup.setObjectName("addGroup")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.addGroup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 381, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeLayout = QtWidgets.QHBoxLayout()
        self.timeLayout.setObjectName("timeLayout")
        self.startLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.startLabel.setObjectName("startLabel")
        self.timeLayout.addWidget(self.startLabel)
        self.startTime = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.startTime.setFrame(True)
        self.startTime.setAccelerated(False)
        self.startTime.setMaximumTime(QtCore.QTime(20, 45, 0))
        self.startTime.setMinimumTime(QtCore.QTime(7, 30, 0))
        self.startTime.setObjectName("startTime")
        self.timeLayout.addWidget(self.startTime)
        self.endLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.endLabel.setObjectName("endLabel")
        self.timeLayout.addWidget(self.endLabel)
        self.endTime = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.endTime.setMaximumTime(QtCore.QTime(21, 0, 0))
        self.endTime.setMinimumTime(QtCore.QTime(7, 45, 0))
        self.endTime.setObjectName("endTime")
        self.timeLayout.addWidget(self.endTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.timeLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.timeLayout)
        self.locationLayout = QtWidgets.QHBoxLayout()
        self.locationLayout.setObjectName("locationLayout")
        self.locationLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.locationLabel.setObjectName("locationLabel")
        self.locationLayout.addWidget(self.locationLabel)
        self.locationLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.locationLine.setObjectName("locationLine")
        self.locationLayout.addWidget(self.locationLine)
        self.verticalLayout.addLayout(self.locationLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem1)
        self.addButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addButton.setObjectName("addButton")
        self.buttonLayout.addWidget(self.addButton)
        self.cancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.buttonLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.buttonLayout)

        self.retranslateUi(addWindow)
        QtCore.QMetaObject.connectSlotsByName(addWindow)
        
        # init
        view.centerWindow(addWindow)
        
        # connect buttons
        self.addButton.clicked.connect(lambda: logic.addSlot(advisorView, addWindow, date, self.startTime.time().toString(), self.endTime.time().toString(), self.locationLine.text(), uid))
        self.cancelButton.clicked.connect(lambda: addWindow.close())

    def retranslateUi(self, addWindow):
        _translate = QtCore.QCoreApplication.translate
        addWindow.setWindowTitle(_translate("addWindow", "Advisor"))
        self.addGroup.setTitle(_translate("addWindow", "Add Slot"))
        self.startLabel.setText(_translate("addWindow", "Start"))
        self.endLabel.setText(_translate("addWindow", "End"))
        self.locationLabel.setText(_translate("addWindow", "Location"))
        self.addButton.setText(_translate("addWindow", "Add"))
        self.cancelButton.setText(_translate("addWindow", "Cancel"))

class editView(object):
    def setupUi(self, editWindow, view, logic, date, sid, start, end, location, advisorView):
        editWindow.setObjectName("editWindow")
        editWindow.resize(403, 163)
        self.editGroup = QtWidgets.QGroupBox(editWindow)
        self.editGroup.setGeometry(QtCore.QRect(10, 10, 381, 141))
        self.editGroup.setFocusPolicy(QtCore.Qt.NoFocus)
        self.editGroup.setObjectName("editGroup")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.editGroup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 381, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeLayout = QtWidgets.QHBoxLayout()
        self.timeLayout.setObjectName("timeLayout")
        self.startLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.startLabel.setObjectName("startLabel")
        self.timeLayout.addWidget(self.startLabel)
        self.startTime = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.startTime.setFrame(True)
        self.startTime.setAccelerated(False)
        self.startTime.setMaximumTime(QtCore.QTime(20, 45, 0))
        self.startTime.setMinimumTime(QtCore.QTime(7, 30, 0))
        self.startTime.setObjectName("startTime")
        self.timeLayout.addWidget(self.startTime)
        self.endLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.endLabel.setObjectName("endLabel")
        self.timeLayout.addWidget(self.endLabel)
        self.endTime = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.endTime.setMaximumTime(QtCore.QTime(21, 0, 0))
        self.endTime.setMinimumTime(QtCore.QTime(7, 45, 0))
        self.endTime.setObjectName("endTime")
        self.timeLayout.addWidget(self.endTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.timeLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.timeLayout)
        self.locationLayout = QtWidgets.QHBoxLayout()
        self.locationLayout.setObjectName("locationLayout")
        self.locationLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.locationLabel.setObjectName("locationLabel")
        self.locationLayout.addWidget(self.locationLabel)
        self.locationLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.locationLine.setObjectName("locationLine")
        self.locationLayout.addWidget(self.locationLine)
        self.verticalLayout.addLayout(self.locationLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem1)
        self.editButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.editButton.setObjectName("editButton")
        self.buttonLayout.addWidget(self.editButton)
        self.cancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.buttonLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.buttonLayout)

        self.retranslateUi(editWindow)
        QtCore.QMetaObject.connectSlotsByName(editWindow)
        
        # init
        view.centerWindow(editWindow)

        # set previous data
        self.startTime.setTime(QtCore.QTime(int(start[0:2]), int(start[2:4])))
        self.endTime.setTime(QtCore.QTime(int(end[0:2]), int(end[2:4])))
        self.locationLine.setText(location)
        
        # connect buttons
        self.editButton.clicked.connect(lambda: logic.editSlot(advisorView, editWindow, date, sid, self.startTime.time().toString(), self.endTime.time().toString(), self.locationLine.text()))
        self.cancelButton.clicked.connect(lambda: editWindow.close())

    def retranslateUi(self, editWindow):
        _translate = QtCore.QCoreApplication.translate
        editWindow.setWindowTitle(_translate("editWindow", "Advisor"))
        self.editGroup.setTitle(_translate("editWindow", "Edit Slot"))
        self.startLabel.setText(_translate("editWindow", "Start"))
        self.endLabel.setText(_translate("editWindow", "End"))
        self.locationLabel.setText(_translate("editWindow", "Location"))
        self.editButton.setText(_translate("editWindow", "Edit"))
        self.cancelButton.setText(_translate("editWindow", "Cancel"))

class notifyView(object):
    def setupUi(self, app, notifyWindow, view, data, logic):
        notifyWindow.setObjectName("notifyWindow")
        notifyWindow.resize(403, 300)
        self.notifyGroup = QtWidgets.QGroupBox(notifyWindow)
        self.notifyGroup.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.notifyGroup.setObjectName("notifyGroup")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.notifyGroup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 381, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.subjectLayout = QtWidgets.QHBoxLayout()
        self.subjectLayout.setObjectName("subjectLayout")
        self.subjectLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.subjectLabel.setObjectName("subjectLabel")
        self.subjectLayout.addWidget(self.subjectLabel)
        self.subjectLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.subjectLine.setObjectName("subjectLine")
        self.subjectLayout.addWidget(self.subjectLine)
        self.verticalLayout.addLayout(self.subjectLayout)
        self.bodyLayout = QtWidgets.QHBoxLayout()
        self.bodyLayout.setObjectName("bodyLayout")
        self.labelLayout = QtWidgets.QVBoxLayout()
        self.labelLayout.setObjectName("labelLayout")
        self.bodyLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.bodyLabel.setObjectName("bodyLabel")
        self.labelLayout.addWidget(self.bodyLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.labelLayout.addItem(spacerItem)
        self.bodyLayout.addLayout(self.labelLayout)
        self.bodyText = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.bodyText.setObjectName("bodyText")
        self.bodyLayout.addWidget(self.bodyText)
        self.verticalLayout.addLayout(self.bodyLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem1)
        self.sendButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sendButton.setObjectName("sendButton")
        self.buttonLayout.addWidget(self.sendButton)
        self.cancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.buttonLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.buttonLayout)

        self.retranslateUi(notifyWindow)
        QtCore.QMetaObject.connectSlotsByName(notifyWindow)
        
        # init
        view.centerWindow(notifyWindow)
        
        # connect buttons
        self.sendButton.clicked.connect(lambda: logic.sendNotify(notifyWindow, self.subjectLine.text(), self.bodyText.toPlainText()))
        self.cancelButton.clicked.connect(lambda: notifyWindow.close())
        
    def retranslateUi(self, notifyWindow):
        _translate = QtCore.QCoreApplication.translate
        notifyWindow.setWindowTitle(_translate("notifyWindow", "Advisor"))
        self.notifyGroup.setTitle(_translate("notifyWindow", "Notify"))
        self.subjectLabel.setText(_translate("notifyWindow", "Subject"))
        self.bodyLabel.setText(_translate("notifyWindow", "Body     "))
        self.sendButton.setText(_translate("notifyWindow", "Send"))
        self.cancelButton.setText(_translate("notifyWindow", "Cancel"))

class studentView(object):
    def setupUi(self, app, studentWindow, view, data, uid, student, loginWindow):
        studentWindow.setObjectName("studentWindow")
        studentWindow.resize(903, 603)
        studentWindow.setFixedSize(903, 603)
        self.viewGroup = QtWidgets.QGroupBox(studentWindow)
        self.viewGroup.setGeometry(QtCore.QRect(10, 10, 881, 581))
        self.viewGroup.setFlat(False)
        self.viewGroup.setObjectName("viewGroup")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.viewGroup)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 881, 551))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.viewLayout = QtWidgets.QVBoxLayout()
        self.viewLayout.setObjectName("viewLayout")
        self.calendar = QtWidgets.QCalendarWidget(self.horizontalLayoutWidget)
        self.calendar.setAutoFillBackground(True)
        self.calendar.setGridVisible(False)
        self.calendar.setObjectName("calendar")
        self.viewLayout.addWidget(self.calendar)
        self.slotTree = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.slotTree.setAutoFillBackground(False)
        self.slotTree.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.slotTree.setObjectName("slotTree")
        self.slotTree.headerItem().setText(0, "1")
        self.viewLayout.addWidget(self.slotTree)
        self.horizontalLayout.addLayout(self.viewLayout)
        self.actionLayout = QtWidgets.QVBoxLayout()
        self.actionLayout.setObjectName("actionLayout")
        self.calendarActions = QtWidgets.QVBoxLayout()
        self.calendarActions.setObjectName("calendarActions")
        self.logoutButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.logoutButton.setObjectName("logoutButton")
        self.calendarActions.addWidget(self.logoutButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.calendarActions.addItem(spacerItem)
        self.actionLayout.addLayout(self.calendarActions)
        self.slotActions = QtWidgets.QVBoxLayout()
        self.slotActions.setObjectName("slotActions")
        self.getButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.getButton.setObjectName("getButton")
        self.slotActions.addWidget(self.getButton)
        self.voidButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.voidButton.setObjectName("voidButton")
        self.slotActions.addWidget(self.voidButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.slotActions.addItem(spacerItem1)
        self.actionLayout.addLayout(self.slotActions)
        self.horizontalLayout.addLayout(self.actionLayout)
        self.viewGroup.raise_()
        self.getButton.raise_()

        self.retranslateUi(studentWindow)
        QtCore.QMetaObject.connectSlotsByName(studentWindow)
        
        # init
        view.centerWindow(studentWindow)
        self.app = app
        self.window = studentWindow
        self.view = view
        self.data = data
        self.uid = uid
        self.student = student
        self.login = loginWindow
        self.slotLogic = logic.slotLogic(app, view, data)
        
        # connect buttons
        self.calendar.clicked.connect(lambda: self.getToday())
        self.getButton.clicked.connect(lambda: self.toGet())
        self.voidButton.clicked.connect(lambda: self.toVoid())
        self.logoutButton.clicked.connect(lambda: self.logout())
        
        # initial events
        self.getToday()

    def retranslateUi(self, studentWindow):
        _translate = QtCore.QCoreApplication.translate
        studentWindow.setWindowTitle(_translate("studentWindow", "Student"))
        self.viewGroup.setTitle(_translate("studentWindow", "View"))
        self.logoutButton.setText(_translate("studentWindow", "Logout"))
        self.getButton.setText(_translate("studentWindow", "Get Slot"))
        self.voidButton.setText(_translate("studentWindow", "Void Slot"))
        
    def getToday(self):
        self.date = self.calendar.selectedDate().toString()
        self.updateView()

    def updateView(self):
        # get data
        col = ["ID", "Start", "End", "Location", "Student"]
        table = self.data.joinLocked(self.date, self.uid)

        # set headers
        for i, c in enumerate(col):
            self.slotTree.headerItem().setText(i, c)

        self.slotTree.clear()
        
        # populate table
        if table:
            for entry in range(len(table)):
                QtWidgets.QTreeWidgetItem(self.slotTree)
                for data in range(len(table[entry])):
                    if (data == 1 or data == 2) and len(str(table[entry][data])) == 3:
                        text = "0" + str(table[entry][data])
                        self.slotTree.topLevelItem(entry).setText(data, text)
                    else:
                        self.slotTree.topLevelItem(entry).setText(data, str(table[entry][data]))

    def toGet(self):
        entry = self.slotTree.selectedItems()
        
        # check error
        if not entry:
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'No slot selected.')
        elif not entry[0].text(4) == "None":
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'Slot is already taken.')
        else:
            item = entry[0].text(0)
            sid = int(item)
            
            # open get slot
            self.getWindow = QtWidgets.QDialog()
            self.getView = getView()
            self.getView.setupUi(self.app, self.window, self.getWindow, self.view, self.data, self.slotLogic, sid, self.uid, self.student, self)
            self.getWindow.show()

    def toVoid(self):
        entry = self.slotTree.selectedItems()
        
        # check error
        if not entry:
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'No slot selected.')
        elif entry[0].text(4) == "None":
            QtWidgets.QMessageBox.warning(self.window, 'Error', 'Slot is not taken.')
        else:
            item = entry[0].text(0)
            sid = int(item)

            # void slot
            reply = QtWidgets.QMessageBox.question(self.window, 'Confirm', 'Void slot {}?'.format(sid), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                self.slotLogic.voidSlot(sid)
                QtWidgets.QMessageBox.warning(self.window, 'Alert', 'Successful.')
                self.getToday()

    def logout(self):
        # back to login
        self.window.close()
        self.login.show()

class getView(object):
    def setupUi(self, app, studentWindow, getWindow, view, data, logic, sid, uid, student, studentView):
        getWindow.setObjectName("getWindow")
        getWindow.resize(403, 230)
        getWindow.setFixedSize(403, 233)
        self.getGroup = QtWidgets.QGroupBox(getWindow)
        self.getGroup.setGeometry(QtCore.QRect(10, 10, 381, 211))
        self.getGroup.setObjectName("getGroup")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.getGroup)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 381, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.getLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.getLayout.setObjectName("getLayout")
        self.courseLayout = QtWidgets.QHBoxLayout()
        self.courseLayout.setObjectName("courseLayout")
        self.courseLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.courseLabel.setObjectName("courseLabel")
        self.courseLayout.addWidget(self.courseLabel)
        self.courseCombo = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.courseCombo.setObjectName("courseCombo")
        self.courseCombo.addItem("")
        self.courseCombo.addItem("")
        self.courseLayout.addWidget(self.courseCombo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.courseLayout.addItem(spacerItem)
        self.getLayout.addLayout(self.courseLayout)
        self.titleLayout = QtWidgets.QHBoxLayout()
        self.titleLayout.setObjectName("titleLayout")
        self.titleLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLayout.addWidget(self.titleLabel)
        self.titleLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.titleLine.setObjectName("titleLine")
        self.titleLayout.addWidget(self.titleLine)
        self.getLayout.addLayout(self.titleLayout)
        self.infoLayout = QtWidgets.QHBoxLayout()
        self.infoLayout.setObjectName("infoLayout")
        self.infoLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.infoLabel.setObjectName("infoLabel")
        self.infoLayout.addWidget(self.infoLabel)
        self.infoText = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.infoText.setObjectName("infoText")
        self.infoLayout.addWidget(self.infoText)
        self.getLayout.addLayout(self.infoLayout)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem1)
        self.getButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.getButton.setObjectName("getButton")
        self.buttonLayout.addWidget(self.getButton)
        self.cancelButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancelButton.setObjectName("cancelButton")
        self.buttonLayout.addWidget(self.cancelButton)
        self.getLayout.addLayout(self.buttonLayout)

        self.retranslateUi(getWindow)
        QtCore.QMetaObject.connectSlotsByName(getWindow)
        
        # init
        view.centerWindow(getWindow)
        
        # connect buttons
        self.getButton.clicked.connect(lambda: logic.getSlot(studentWindow, getWindow, sid, uid, student, self.courseCombo.currentText(), self.titleLine.text(), self.infoText.toPlainText(), studentView))
        self.cancelButton.clicked.connect(lambda: getWindow.close())

    def retranslateUi(self, getWindow):
        _translate = QtCore.QCoreApplication.translate
        getWindow.setWindowTitle(_translate("getWindow", "Student"))
        self.getGroup.setTitle(_translate("getWindow", "Get Slot"))
        self.courseLabel.setText(_translate("getWindow", "Course"))
        self.courseCombo.setItemText(0, _translate("getWindow", "Thesis"))
        self.courseCombo.setItemText(1, _translate("getWindow", "Design"))
        self.titleLabel.setText(_translate("getWindow", "Title"))
        self.infoLabel.setText(_translate("getWindow", "Info"))
        self.getButton.setText(_translate("getWindow", "Get"))
        self.cancelButton.setText(_translate("getWindow", "Cancel"))

class view():
    def __init__(self):
        desktop = app.primaryScreen()
        self.size = desktop.availableGeometry()
    
    def centerWindow(self, window):
        widget = window.geometry()
        x = (self.size.width() - widget.width()) / 2
        y = (self.size.height() - widget.height()) / 2
        window.move(x, y)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # init view, data and logic
    view = view()
    data = data.dataTools('skedcon')
    
    # init login
    loginWindow = QtWidgets.QDialog()    
    loginView = loginView()
    loginView.setupUi(app, loginWindow, view, data)
    loginWindow.show()
    
    sys.exit(app.exec_())
