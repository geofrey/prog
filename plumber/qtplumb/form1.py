# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created: Fri May 27 13:52:39 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class Form1(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("Form1")



        self.groupBox1 = QGroupBox(self,"groupBox1")
        self.groupBox1.setGeometry(QRect(10,10,510,460))

        self.listBox1 = QListBox(self.groupBox1,"listBox1")
        self.listBox1.setGeometry(QRect(10,30,380,380))

        self.lineEdit1 = QLineEdit(self.groupBox1,"lineEdit1")
        self.lineEdit1.setGeometry(QRect(10,420,381,31))

        self.addbutton1 = QPushButton(self.groupBox1,"addbutton1")
        self.addbutton1.setGeometry(QRect(400,80,100,30))
        self.addbutton1.setAutoDefault(0)
        self.addbutton1.setDefault(1)

        self.removebutton1 = QPushButton(self.groupBox1,"removebutton1")
        self.removebutton1.setGeometry(QRect(400,120,101,31))
        self.removebutton1.setAutoDefault(0)

        self.pushButton5 = QPushButton(self.groupBox1,"pushButton5")
        self.pushButton5.setGeometry(QRect(400,160,101,31))

        self.pushButton9 = QPushButton(self,"pushButton9")
        self.pushButton9.setGeometry(QRect(530,480,140,40))

        self.groupBox2 = QGroupBox(self,"groupBox2")
        self.groupBox2.setGeometry(QRect(530,10,510,460))

        self.addbutton2 = QPushButton(self.groupBox2,"addbutton2")
        self.addbutton2.setGeometry(QRect(400,80,100,30))

        self.removebutton2 = QPushButton(self.groupBox2,"removebutton2")
        self.removebutton2.setGeometry(QRect(400,120,101,31))

        self.pushButton6 = QPushButton(self.groupBox2,"pushButton6")
        self.pushButton6.setGeometry(QRect(400,160,101,31))

        self.listBox3 = QListBox(self.groupBox2,"listBox3")
        self.listBox3.setGeometry(QRect(10,30,380,380))

        self.lineEdit2 = QLineEdit(self.groupBox2,"lineEdit2")
        self.lineEdit2.setGeometry(QRect(10,420,381,31))

        self.runbutton = QPushButton(self,"runbutton")
        self.runbutton.setGeometry(QRect(380,480,140,40))
        runbutton_font = QFont(self.runbutton.font())
        self.runbutton.setFont(runbutton_font)

        self.languageChange()

        self.resize(QSize(1050,531).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.removebutton1,SIGNAL("clicked()"),self.removeselection1)
        self.connect(self.addbutton1,SIGNAL("clicked()"),self.additem1)
        self.connect(self.lineEdit1,SIGNAL("returnPressed()"),self.additem1)
        self.connect(self.pushButton5,SIGNAL("clicked()"),self.listBox1.clear)
        self.connect(self.pushButton6,SIGNAL("clicked()"),self.listBox3.clear)
        self.connect(self.addbutton2,SIGNAL("clicked()"),self.additem2)
        self.connect(self.lineEdit2,SIGNAL("returnPressed()"),self.additem2)
        self.connect(self.removebutton2,SIGNAL("clicked()"),self.removeselection2)
        self.connect(self.runbutton,SIGNAL("clicked()"),self.run)
        self.connect(self.pushButton9,SIGNAL("clicked()"),self.listBox1.clear)
        self.connect(self.pushButton9,SIGNAL("clicked()"),self.listBox3.clear)
        self.connect(self.pushButton9,SIGNAL("clicked()"),self.lineEdit1.clear)
        self.connect(self.pushButton9,SIGNAL("clicked()"),self.lineEdit2.clear)
        self.connect(self.lineEdit2,SIGNAL("lostFocus()"),self.additem2)
        self.connect(self.lineEdit1,SIGNAL("lostFocus()"),self.additem1)

        self.setTabOrder(self.lineEdit1,self.lineEdit2)
        self.setTabOrder(self.lineEdit2,self.runbutton)
        self.setTabOrder(self.runbutton,self.addbutton1)
        self.setTabOrder(self.addbutton1,self.pushButton5)
        self.setTabOrder(self.pushButton5,self.removebutton1)
        self.setTabOrder(self.removebutton1,self.listBox1)
        self.setTabOrder(self.listBox1,self.pushButton9)
        self.setTabOrder(self.pushButton9,self.addbutton2)
        self.setTabOrder(self.addbutton2,self.removebutton2)
        self.setTabOrder(self.removebutton2,self.pushButton6)
        self.setTabOrder(self.pushButton6,self.listBox3)


    def languageChange(self):
        self.setCaption(self.__tr("QTPlumb quick demo"))
        self.groupBox1.setTitle(self.__tr("Input programs"))
        self.addbutton1.setText(self.__tr("Add"))
        self.removebutton1.setText(self.__tr("Remove"))
        self.pushButton5.setText(self.__tr("Clear"))
        self.pushButton9.setText(self.__tr("Clear all"))
        self.groupBox2.setTitle(self.__tr("Output programs"))
        self.addbutton2.setText(self.__tr("Add"))
        self.removebutton2.setText(self.__tr("Remove"))
        self.pushButton6.setText(self.__tr("Clear"))
        self.runbutton.setText(self.__tr("Run programs"))


    def additem1(self):
        
        	e = self.lineEdit1.text().ascii()
        	if len(e) > 0:
        		self.listBox1.insertItem(e)
        		self.lineEdit1.clear()
        

    def removeselection1(self):
        	self.listBox1.removeItem(self.listBox1.index(self.listBox1.selectedItem()))
        

    def additem2(self):
        	e = self.lineEdit2.text().ascii()
        	if len(e) > 0:
        		self.listBox3.insertItem(e)
        		self.lineEdit2.clear()
        

    def removeselection2(self):
        	self.listBox3.removeItem(self.listBox3.index(self.listBox3.selectedItem()))
        

    def run(self):
        	from thread import start_new_thread
        	command_line = "xterm -geometry 120x60 -hold -e ../demo-start.py "
        	for i in range(0, self.listBox1.numRows()):
        		command_line += " \"" + self.listBox1.item(i).text().ascii() + "\""
        	command_line += " : "
        	for i in range(0, self.listBox3.numRows()):
        		command_line += " \"" + self.listBox3.item(i).text().ascii() + "\""
        	from os import system
        	def thread_stuff(x):
        		system(command_line)
        	start_new_thread(thread_stuff, (0, ))
        

    def __tr(self,s,c = None):
        return qApp.translate("Form1",s,c)
