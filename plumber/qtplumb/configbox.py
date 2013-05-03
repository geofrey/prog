# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configbox.ui'
#
# Created: Fri Jun 10 02:19:14 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class configBox(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("configBox")



        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(10,20,141,31))

        self.xtermPath = QLineEdit(self,"xtermPath")
        self.xtermPath.setGeometry(QRect(160,60,400,30))

        self.browseXterm = QPushButton(self,"browseXterm")
        self.browseXterm.setGeometry(QRect(570,60,111,31))

        self.textLabel2 = QLabel(self,"textLabel2")
        self.textLabel2.setGeometry(QRect(10,60,140,31))

        self.cancelButton = QPushButton(self,"cancelButton")
        self.cancelButton.setGeometry(QRect(350,100,111,31))

        self.browsePlumber = QPushButton(self,"browsePlumber")
        self.browsePlumber.setGeometry(QRect(570,20,111,31))

        self.plumberPath = QLineEdit(self,"plumberPath")
        self.plumberPath.setGeometry(QRect(161,20,400,30))

        self.okButton = QPushButton(self,"okButton")
        self.okButton.setGeometry(QRect(220,100,120,30))
        self.okButton.setDefault(1)

        self.languageChange()

        self.resize(QSize(694,139).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.cancelButton,SIGNAL("clicked()"),self.close)
        self.connect(self.browsePlumber,SIGNAL("clicked()"),self.browse_plumber)
        self.connect(self.browseXterm,SIGNAL("clicked()"),self.browse_xterm)
        self.connect(self.okButton,SIGNAL("clicked()"),self.ok_click)

        self.setTabOrder(self.plumberPath,self.xtermPath)
        self.setTabOrder(self.xtermPath,self.okButton)
        self.setTabOrder(self.okButton,self.cancelButton)
        self.setTabOrder(self.cancelButton,self.browsePlumber)
        self.setTabOrder(self.browsePlumber,self.browseXterm)


    def languageChange(self):
        self.setCaption(self.__tr("QTPlumb Settings"))
        self.textLabel1.setText(self.__tr("Plumber location"))
        self.browseXterm.setText(self.__tr("Browse"))
        self.textLabel2.setText(self.__tr("Xterm location"))
        self.cancelButton.setText(self.__tr("Cancel"))
        self.browsePlumber.setText(self.__tr("Browse"))
        self.okButton.setText(self.__tr("OK"))


    def ok_click(self):
        	from commands import getoutput
        	file = open(getoutput("echo ~") + "/.qtplumb", "w")
        	file.write(self.plumberPath.text().ascii())
        	file.write("\n")
        	file.write(self.xtermPath.text().ascii())
        	file.close()
        	self.close()
        

    def browse_plumber(self):
        	location = QFileDialog.getOpenFileName(self.plumberPath.text(), "All files (*)", self, "Plumber location").ascii()
        	if location != None:
        		self.plumberPath.setText(QString(location))
        

    def browse_xterm(self):
        	location = QFileDialog.getOpenFileName(self.xtermPath.text(), "All files (*)", self, "Plumber location").ascii()
        	if location != None:
        		self.xtermPath.setText(QString(location))
        

    def init_two(self):
        	from commands import getstatus
        	from commands import getoutput
        	import glob
        	if len(glob.glob(getoutput("echo ~") + "/.qtplumb")) > 0:
        		file = open(getoutput("echo ~") + "/.qtplumb", "r")
        		self.plumberPath.setText(QString(file.readline()))
        		temp = file.readline()
        		for i in range(0, 5):
        			if temp != "\n":
        				break
        			temp = file.readline()
        		self.xtermPath.setText(QString(temp))
        		file.close()
        	else:
        		self.plumberPath.setText(QString("../plumber"))
        		self.xtermPath.setText(QString("/usr/bin/xterm"))
        

    def __tr(self,s,c = None):
        return qApp.translate("configBox",s,c)
