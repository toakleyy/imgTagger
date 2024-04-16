"""
--- HOW TO CREATE .PY FILE FROM .UI FILE ---
Terminal command:
pyuic5 -x  "TEST UI".ui -o test.py

--- HOW TO CREATE MAC-OS APP ---
Terminal commands (pick one):
python setup.py py2app
python setup.py py2app -A     <------ Alias Mode (keeps terminal open)

--- HOW TO CREATE WINDOWS .EXE ---
Terminal commands (pick one):
pyinstaller --onefile -w --name "AMIA App" "Main.py"
pyinstaller --onefile --name "AMIA App" "Main.py"     <------ debug mode (keeps terminal open)
"""

import os
import platform
import json
from datetime import datetime, timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtProperty, QParallelAnimationGroup

root_dir = os.getcwd()


if 'macOS' in platform.platform():
    running_on = 'MacOS'
else:
    running_on = 'Windows'


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    login_screen = LoginWindow()

    sys.exit(app.exec_())
