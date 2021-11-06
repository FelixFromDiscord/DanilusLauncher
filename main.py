import launcher
import sys
import json
import subprocess
import time
import requests as req
from PyQt5 import QtWidgets

class App(QtWidgets.QMainWindow, launcher.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.Login.clicked.connect(self.login)
	def login(self):
		nick = self.NickEdit.text()
		address = self.IPEdit.text()
		port = self.lineEdit_2.text()
		theme = self.lineEdit.text()

		try:
			subprocess.run(["client.py", "launcher", address, port, nick, theme + ".thm"])
		except:
			pass

		time.sleep(1)
		quit()

def main():
	app = QtWidgets.QApplication(sys.argv)
	window = App()
	window.show()
	app.exec_()

if __name__ == '__main__':
	main()