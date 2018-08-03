# Consultation Scheduler

**Legacy Project**

A basic graphical application for handling thesis and design consultation schedules written in python 3.

It uses the following libraries:
```python
# view.py
import sys, data, logic
from PyQt5 import QtCore, QtGui, QtWidgets

# logic.py
import view
import re, threading, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

# data.py
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
```

# Run

It can be run by executing
```python
python3 view.py
```

# Note

Change the MySQL root password in the **.passwd** file.