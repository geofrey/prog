#!/usr/bin/python

from qt import *
from qtplumb import *
import sys
if __name__ == "__main__":
	app = QApplication(sys.argv)
	f = Form1()
	f.init_two()
	f.show()
	app.setMainWidget(f)
	app.exec_loop()
