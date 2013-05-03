# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtplumb.ui'
#
# Created: Fri Jun 10 02:19:14 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *
from qttable import QTable

image0_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x74\x49\x44\x41\x54\x38\x8d\xed\xd5\xc1\x09\xc0" \
    "\x20\x0c\x05\xd0\x6f\xe9\x36\x81\x2c\x10\xb2\xff" \
    "\xdd\x85\xd2\x53\x85\xb6\xa9\x91\x48\x0f\x05\x3f" \
    "\x08\x1a\xf0\x29\x12\x10\xf8\x28\xc5\xa9\xd9\xc4" \
    "\xde\x96\xcd\x2b\x9a\xd9\xeb\x00\x00\x66\x0e\x2f" \
    "\xe0\xc2\x51\x98\x39\xc4\xf7\x0c\x4c\x44\x6d\x5e" \
    "\x6b\x35\x38\xcf\x92\x82\x45\xe4\xb2\xf6\xf0\x14" \
    "\xac\xaa\x8f\xda\x1d\x4f\xc1\xa5\x74\x1b\x22\x07" \
    "\x9f\x9d\x11\x1d\x96\xea\x8a\x91\x2c\x78\xc1\x0b" \
    "\xee\x64\xe6\x07\x19\xf5\x7e\x92\x03\xad\x45\x2a" \
    "\x04\xcc\x4e\x50\x20\x00\x00\x00\x00\x49\x45\x4e" \
    "\x44\xae\x42\x60\x82"
image1_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\x99\x49\x44\x41\x54\x38\x8d\xed\x94\x41\x0e\x85" \
    "\x20\x0c\x44\x5f\x89\xc7\x36\x7f\x61\xbc\x77\x5d" \
    "\x28\x48\xa4\x28\x60\xff\xce\xd9\x54\x8b\xbe\x8e" \
    "\x13\x04\x3e\x1d\x92\x81\x77\xf4\x81\xa1\x23\xdc" \
    "\x2b\x34\xf6\xf4\x7a\x3d\xe2\xb8\x65\xa8\x84\x3f" \
    "\x40\x01\x98\x2a\x0b\x3d\x5f\x62\xc5\x83\x00\xaa" \
    "\x1a\xd7\x05\x50\x44\x9a\xb9\xd5\x07\xa7\x73\xa8" \
    "\xa4\xba\x4f\x92\xa2\xdf\x33\x3c\x64\xc6\x3b\xeb" \
    "\xbd\x82\xe5\xb8\xad\xde\xcb\xcc\x78\x20\xeb\x42" \
    "\x66\xc6\x39\x74\x5d\xfa\x80\xf3\x6f\xaf\x66\xc6" \
    "\x6f\xa1\x9c\x3f\x88\x2f\xb4\x70\xec\x05\xcd\xc0" \
    "\xbe\xd0\x78\x93\xf6\x8e\x17\x14\x92\x63\x5f\x68" \
    "\x6c\x3e\xef\xf6\xba\x3c\x8f\xdd\x36\x6d\xc4\xc0" \
    "\x45\x2c\x87\x81\xf8\x08\x00\x00\x00\x00\x49\x45" \
    "\x4e\x44\xae\x42\x60\x82"
image2_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x00" \
    "\xa0\x49\x44\x41\x54\x38\x8d\xd5\x95\x4d\x0a\x80" \
    "\x20\x10\x85\x9f\xd1\x46\x68\xe1\x8d\xe6\x62\xd2" \
    "\x22\xbc\x98\x37\x6a\x21\xb4\xac\x45\x19\x92\xc6" \
    "\x64\x69\xe0\xb7\xf1\x87\xf1\xf1\x1c\x47\x05\x2a" \
    "\x21\x8e\x76\x2d\xad\xdb\xfb\x9e\x99\xf6\x56\x8f" \
    "\x80\xb5\x36\x4b\x85\x88\xce\x35\x44\x04\x00\xe8" \
    "\x0a\x39\x8c\xe8\xf9\x90\x34\xd2\x29\x2c\xc3\x7c" \
    "\x8e\xbd\x53\x0f\xeb\x58\x3a\x05\xe9\x54\x34\x1f" \
    "\x8a\x02\x7b\x2a\x7d\x3a\x1f\x09\xbf\x85\x4d\xc5" \
    "\xd5\xd9\x53\xaa\x39\x6e\x4f\x38\xca\xb1\x99\xe2" \
    "\xd2\xe1\x08\xab\xe1\x56\xf8\x2e\x30\x97\x7f\xcb" \
    "\x4d\x8f\xf9\x42\xd7\x5d\xbe\xbe\xd2\xe1\x43\x95" \
    "\x3a\x93\xf6\xca\xad\x3d\x61\x11\xf4\x4b\x7d\x4f" \
    "\x82\x0f\xf9\xc0\x06\x9b\xb5\x1e\xcd\xed\x31\x8c" \
    "\x5c\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60" \
    "\x82"
image3_data = \
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d" \
    "\x49\x48\x44\x52\x00\x00\x00\x16\x00\x00\x00\x16" \
    "\x08\x06\x00\x00\x00\xc4\xb4\x6c\x3b\x00\x00\x02" \
    "\x9c\x49\x44\x41\x54\x38\x8d\x8d\x95\xad\x76\xdb" \
    "\x40\x10\x85\x3f\xf7\x18\xcc\x32\x89\xd9\x50\xd0" \
    "\x61\x36\x34\x4c\x98\xc3\x62\x96\x40\x87\x25\x6f" \
    "\x50\x3f\x42\x61\x61\x02\x1b\xe6\xb2\x84\x25\x50" \
    "\x61\x2e\x8b\xe1\x42\x99\x49\x6c\x86\x6d\xc1\x4a" \
    "\xb2\xfc\x77\xda\x21\x92\x66\x57\x77\xee\xdc\x3b" \
    "\x5a\xf5\x38\x13\xaf\xaf\xaf\x41\x44\x48\xd3\x74" \
    "\x2f\x6f\x66\x00\xa8\x2a\x00\x55\x55\x91\x24\x09" \
    "\x57\x57\x57\xbd\xee\xbe\xfe\x39\x60\x11\x61\x32" \
    "\x99\xb4\x40\x87\x6b\x4d\x94\x65\x89\xf7\xfe\x68" \
    "\xcf\x59\x60\x80\xcd\x66\x73\x04\x76\x58\x48\x55" \
    "\x71\xce\xfd\x3f\xf0\x29\x00\x33\x3b\x2a\x70\xaa" \
    "\x23\x80\x6f\xa7\x92\x79\x9e\x07\x33\x6b\x99\x38" \
    "\xe7\x70\xce\xed\xe9\xdd\xe8\x2f\x22\x47\xfa\x9e" \
    "\x65\xac\xaa\x24\x49\x42\x59\x96\x88\x48\x6b\x54" \
    "\x37\x4e\xb5\xff\x4f\xc6\x10\x5b\x3c\x9c\x88\x2e" \
    "\x68\x53\xec\x9c\x14\x27\x19\x37\x6c\x4e\x31\xed" \
    "\xe6\x55\x75\x6f\x42\xba\x71\xa4\x0d\xc0\x6a\xb5" \
    "\x0a\x59\x96\x31\x1c\x0e\xcf\x82\x37\x46\x7e\x7e" \
    "\x7e\x02\x20\x92\x30\x9f\x5f\xb7\x78\x7b\x8c\xdf" \
    "\xdf\xdf\x83\xf7\x9e\xfc\x23\x47\x66\x82\x88\xb4" \
    "\x00\x87\xd7\x86\x69\x59\x94\xe4\x79\xce\xb6\xda" \
    "\xf2\xf0\xf0\x10\x66\xb3\x19\xd7\xd7\xd7\xbd\x5e" \
    "\x17\x74\xb3\xf1\x54\xc5\x16\x35\x80\xd3\x4c\x01" \
    "\x9c\xa4\x08\x02\x0e\x7c\xe1\x59\xaf\xff\xb0\xdd" \
    "\x16\xa8\x1a\x17\x17\x19\x8b\xc5\x22\x4a\xd1\x30" \
    "\xbd\x9c\x5e\xe2\xd2\x14\x55\x03\x53\x8e\x6c\x31" \
    "\x03\x84\x9c\x4f\x3e\x78\x65\x6a\x53\xd2\xaf\x94" \
    "\xe7\x97\x67\xfc\x57\xfc\xfa\xd4\x94\x6c\x74\x11" \
    "\x41\x9f\x9e\x7e\x85\xb2\x28\xc3\xff\xc4\x57\xf8" \
    "\x0a\xa3\x30\x0a\x12\x24\x8c\xc2\x28\xac\xd7\xeb" \
    "\xf0\xe3\xfb\xcf\x30\x1e\x8f\xc3\x60\x90\x85\x24" \
    "\x49\x42\x36\xc8\x42\xbf\xda\x56\xdc\xdd\xdd\x9c" \
    "\x75\xf7\x30\x52\x52\x2e\x99\x92\x23\xcc\x98\x31" \
    "\x1e\x8f\x49\x64\x48\x69\x05\xcf\xbf\x5e\xa8\xaa" \
    "\x8a\x74\x90\xd2\x37\xc0\xfb\x22\xce\xa3\x19\x88" \
    "\x10\x6b\x48\xed\x36\x38\x5c\x54\xdc\x14\xc4\xf1" \
    "\x60\xdf\xb9\xc1\x33\xb4\x21\x7f\xd8\x80\x19\xe9" \
    "\x70\x18\xd7\x6b\x77\xfa\x65\x51\xe0\x45\xa2\x9e" \
    "\x66\xb4\xbe\x39\x88\x2e\xd6\x9d\x38\x03\x15\x20" \
    "\xe6\x04\xf0\xb6\xc5\x88\x67\x88\xdf\x6c\x5a\x4f" \
    "\x1c\xf5\xb8\x35\x09\x6b\x00\xb1\x76\x28\x14\x8b" \
    "\x35\x74\x6f\x67\x3b\x39\xd2\x78\xda\x09\x45\xe9" \
    "\x23\x60\x65\xe7\x05\xad\xc9\x76\x37\x1a\x20\x0a" \
    "\x76\xb8\xe2\x30\x2b\xa9\xfb\x6c\x7a\x63\x32\x99" \
    "\xf2\x0d\xeb\xb0\x6c\xc9\x6a\x7c\xb4\xfa\xba\x07" \
    "\xea\x9a\x6d\x35\x68\x0d\x58\xcb\x39\x18\x0c\x58" \
    "\x2c\xee\x22\x63\xef\x7d\x63\x15\x88\x41\x25\x40" \
    "\x15\x9d\x33\x8b\x30\xd2\xb0\xb2\x1d\x18\x3b\xcd" \
    "\x31\x43\x04\x96\xcb\x25\xf3\xf9\xbc\xd7\xcf\xb2" \
    "\x8c\x8f\xb7\x0f\x7e\xbf\xbd\xa1\x6a\xc4\xf3\x47" \
    "\xd8\x1b\x3e\xe9\x3c\xcb\x0e\xb2\xed\xb3\x9e\xa6" \
    "\xe5\x72\xc9\xe3\xe3\x63\x0f\x3a\x87\xd0\x6a\xb5" \
    "\x0a\xab\xd5\x1b\xdb\xfa\xff\xa5\x68\x6d\xca\xce" \
    "\x99\xdd\x5f\x03\x54\xcb\x78\x5f\x19\x93\xe9\x84" \
    "\xdb\xdb\x5b\xee\xef\xef\x5b\xbc\xbf\xd1\xf6\x9e" \
    "\x0c\x3f\xec\x24\x86\x00\x00\x00\x00\x49\x45\x4e" \
    "\x44\xae\x42\x60\x82"

class Form1(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        self.image0 = QPixmap()
        self.image0.loadFromData(image0_data,"PNG")
        self.image1 = QPixmap()
        self.image1.loadFromData(image1_data,"PNG")
        self.image2 = QPixmap()
        self.image2.loadFromData(image2_data,"PNG")
        self.image3 = QPixmap()
        self.image3.loadFromData(image3_data,"PNG")
        if not name:
            self.setName("Form1")


        self.setCentralWidget(QWidget(self,"qt_central_widget"))

        self.addButton = QPushButton(self.centralWidget(),"addButton")
        self.addButton.setGeometry(QRect(620,20,111,31))
        self.addButton.setAutoDefault(1)

        self.replaceButton = QPushButton(self.centralWidget(),"replaceButton")
        self.replaceButton.setGeometry(QRect(740,20,110,31))
        self.replaceButton.setAutoDefault(1)

        self.deleteButton = QPushButton(self.centralWidget(),"deleteButton")
        self.deleteButton.setGeometry(QRect(860,20,111,31))
        self.deleteButton.setAutoDefault(1)

        self.pushButton1 = QPushButton(self.centralWidget(),"pushButton1")
        self.pushButton1.setGeometry(QRect(290,430,121,41))
        self.pushButton1.setAutoDefault(1)

        self.pushButton1_2 = QPushButton(self.centralWidget(),"pushButton1_2")
        self.pushButton1_2.setGeometry(QRect(420,430,121,41))
        self.pushButton1_2.setAutoDefault(1)

        self.table1 = QTable(self.centralWidget(),"table1")
        self.table1.setGeometry(QRect(10,70,980,350))
        self.table1.setNumRows(100)
        self.table1.setNumCols(100)
        self.table1.setReadOnly(1)
        self.table1.setSelectionMode(QTable.Single)

        self.lineEdit1 = QLineEdit(self.centralWidget(),"lineEdit1")
        self.lineEdit1.setGeometry(QRect(10,20,601,31))

        self.fileNewAction = QAction(self,"fileNewAction")
        self.fileNewAction.setIconSet(QIconSet(self.image0))
        self.fileOpenAction = QAction(self,"fileOpenAction")
        self.fileOpenAction.setIconSet(QIconSet(self.image1))
        self.fileSaveAction = QAction(self,"fileSaveAction")
        self.fileSaveAction.setIconSet(QIconSet(self.image2))
        self.fileSaveAsAction = QAction(self,"fileSaveAsAction")
        self.filePrintAction = QAction(self,"filePrintAction")
        self.filePrintAction.setIconSet(QIconSet(self.image3))
        self.fileExitAction = QAction(self,"fileExitAction")
        self.helpContentsAction = QAction(self,"helpContentsAction")
        self.helpIndexAction = QAction(self,"helpIndexAction")
        self.helpAboutAction = QAction(self,"helpAboutAction")
        self.editSettingsAction = QAction(self,"editSettingsAction")
        self.menunew_itemAction = QAction(self,"menunew_itemAction")


        self.toolBar = QToolBar(QString(""),self,Qt.DockTop)

        self.fileNewAction.addTo(self.toolBar)
        self.fileOpenAction.addTo(self.toolBar)
        self.fileSaveAction.addTo(self.toolBar)
        self.fileSaveAsAction.addTo(self.toolBar)


        self.MenuBar = QMenuBar(self,"MenuBar")


        self.fileMenu = QPopupMenu(self)
        self.fileNewAction.addTo(self.fileMenu)
        self.fileOpenAction.addTo(self.fileMenu)
        self.fileSaveAction.addTo(self.fileMenu)
        self.fileSaveAsAction.addTo(self.fileMenu)
        self.fileMenu.insertSeparator()
        self.fileExitAction.addTo(self.fileMenu)
        self.MenuBar.insertItem(QString(""),self.fileMenu,1)

        self.Edit = QPopupMenu(self)
        self.editSettingsAction.addTo(self.Edit)
        self.MenuBar.insertItem(QString(""),self.Edit,2)

        self.helpMenu = QPopupMenu(self)
        self.helpAboutAction.addTo(self.helpMenu)
        self.MenuBar.insertItem(QString(""),self.helpMenu,3)


        self.languageChange()

        self.resize(QSize(1000,556).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.fileExitAction,SIGNAL("activated()"),self.close)
        self.connect(self.pushButton1_2,SIGNAL("clicked()"),self.close)
        self.connect(self.table1,SIGNAL("pressed(int,int,int,const QPoint&)"),self.table_click)
        self.connect(self.addButton,SIGNAL("clicked()"),self.add_entry)
        self.connect(self.replaceButton,SIGNAL("clicked()"),self.replace_entry)
        self.connect(self.lineEdit1,SIGNAL("returnPressed()"),self.add_entry)
        self.connect(self.deleteButton,SIGNAL("clicked()"),self.delete_entry)
        self.connect(self.addButton,SIGNAL("clicked()"),self.lineEdit1.clear)
        self.connect(self.lineEdit1,SIGNAL("returnPressed()"),self.lineEdit1.clear)
        self.connect(self.replaceButton,SIGNAL("clicked()"),self.lineEdit1.clear)
        self.connect(self.deleteButton,SIGNAL("clicked()"),self.lineEdit1.clear)
        self.connect(self.pushButton1,SIGNAL("clicked()"),self.run_programs)
        self.connect(self.fileNewAction,SIGNAL("activated()"),self.new_graph)
        self.connect(self.editSettingsAction,SIGNAL("activated()"),self.display_config)
        self.connect(self.fileOpenAction,SIGNAL("activated()"),self.open_command)
        self.connect(self.fileSaveAction,SIGNAL("activated()"),self.save_command)
        self.connect(self.fileSaveAsAction,SIGNAL("activated()"),self.saveas_command)
        self.connect(self.helpAboutAction,SIGNAL("activated()"),self.show_about)

        self.setTabOrder(self.lineEdit1,self.addButton)
        self.setTabOrder(self.addButton,self.replaceButton)
        self.setTabOrder(self.replaceButton,self.deleteButton)
        self.setTabOrder(self.deleteButton,self.pushButton1)
        self.setTabOrder(self.pushButton1,self.pushButton1_2)
        self.setTabOrder(self.pushButton1_2,self.table1)


    def languageChange(self):
        self.setCaption(self.__tr("QTPlumb"))
        self.addButton.setText(self.__tr("Add"))
        self.replaceButton.setText(self.__tr("Replace"))
        self.deleteButton.setText(self.__tr("Delete"))
        self.pushButton1.setText(self.__tr("Run Programs"))
        self.pushButton1_2.setText(self.__tr("Close"))
        QToolTip.add(self.table1,self.__tr("Click on the spreadsheet to create connections"))
        QToolTip.add(self.lineEdit1,self.__tr("Enter your programs here"))
        self.fileNewAction.setText(self.__tr("New"))
        self.fileNewAction.setMenuText(self.__tr("&New"))
        self.fileNewAction.setAccel(self.__tr("Ctrl+N"))
        self.fileOpenAction.setText(self.__tr("Open"))
        self.fileOpenAction.setMenuText(self.__tr("&Open..."))
        self.fileOpenAction.setAccel(self.__tr("Ctrl+O"))
        self.fileSaveAction.setText(self.__tr("Save"))
        self.fileSaveAction.setMenuText(self.__tr("&Save"))
        self.fileSaveAction.setAccel(self.__tr("Ctrl+S"))
        self.fileSaveAsAction.setText(self.__tr("Save As"))
        self.fileSaveAsAction.setMenuText(self.__tr("Save &As..."))
        self.fileSaveAsAction.setAccel(QString.null)
        self.filePrintAction.setText(self.__tr("Print"))
        self.filePrintAction.setMenuText(self.__tr("&Print..."))
        self.filePrintAction.setAccel(self.__tr("Ctrl+P"))
        self.fileExitAction.setText(self.__tr("E&xit"))
        self.fileExitAction.setMenuText(self.__tr("E&xit"))
        self.fileExitAction.setAccel(QString.null)
        self.helpContentsAction.setText(self.__tr("Contents"))
        self.helpContentsAction.setMenuText(self.__tr("&Contents..."))
        self.helpContentsAction.setAccel(QString.null)
        self.helpIndexAction.setText(self.__tr("Index"))
        self.helpIndexAction.setMenuText(self.__tr("&Index..."))
        self.helpIndexAction.setAccel(QString.null)
        self.helpAboutAction.setText(self.__tr("About"))
        self.helpAboutAction.setMenuText(self.__tr("&About"))
        self.helpAboutAction.setAccel(QString.null)
        self.editSettingsAction.setText(self.__tr("Options"))
        self.editSettingsAction.setMenuText(self.__tr("Options"))
        self.menunew_itemAction.setText(self.__tr("new item"))
        self.menunew_itemAction.setMenuText(self.__tr("new item"))
        self.toolBar.setLabel(self.__tr("Tools"))
        if self.MenuBar.findItem(1):
            self.MenuBar.findItem(1).setText(self.__tr("&File"))
        if self.MenuBar.findItem(2):
            self.MenuBar.findItem(2).setText(self.__tr("Edit"))
        if self.MenuBar.findItem(3):
            self.MenuBar.findItem(3).setText(self.__tr("&Help"))


    def run_programs(self):
        	import glob
        	from commands import getoutput
        	from thread import start_new_thread
        	if len(glob.glob(getoutput("echo ~") + "/.qtplumb")) > 0:
        		file = open(getoutput("echo ~") + "/.qtplumb", "r")
        		command = file.readline()
        		xterm_loc = file.readline()
        		for i in range(0, 5):
        			if xterm_loc != "\n":
        				break
        			xterm_loc = file.readline()
        		file.close()
        		command = command[0:(len(command) - 1)]
        		command = xterm_loc + " -hold -e " + command
        	else:
        		command = "../testadj "
        	for i in range(0, len(self.programs)):
        		command += " \"%d:" % (i + 1) + self.programs[i] + "\" "
        	command += " -e "
        	for i in range(1, len(self.programs) + 2):
        		for j in range(1, len(self.programs) + 2):
        			if self.table1.text(i, j).ascii() == "X":
        				command += " %d," % (i - 1) + "%d " % (j - 1)
        	def command_runner(x):
        		getoutput(command)
        	start_new_thread(command_runner, (0, ))
        

    def table_click(self,row,col,button,point):
        	if (row == 0) or (row > len(self.programs) + 1) or (col > (len(self.programs) + 1)) or ((row == 1) and (col == 0)):
        		self.disable_ed()	
        		return
        	if col == 0:
        		self.selectedEntry = [row,col]
        		self.replaceButton.setEnabled(1)
        		self.deleteButton.setEnabled(1)
        		self.lineEdit1.setText(self.table1.text(row,col))
        		return
        	if self.table1.text(row, col).ascii() != "X":
        		self.table1.setText(row, col, QString("X"))
        	else:
        		self.table1.setText(row, col, QString(""))
        	self.disable_ed()	
        

    def add_entry(self):
        	s = self.lineEdit1.text().ascii()
        	self.programs.append(s)
        	self.table1.setText(len(self.programs) + 1, 0, s)
        	self.table1.setText(0, len(self.programs) + 1, s)
        

    def replace_entry(self):
        	s = self.lineEdit1.text().ascii()
        	self.programs[self.selectedEntry[0] - 1] = s
        	self.table1.setText(self.selectedEntry[0], 0, s)
        	self.table1.setText(0, self.selectedEntry[0], s)
        

    def init_two(self):
        	self.programs = []
        	self.table1.setText(0, 1, QString("Console"))
        	self.table1.setText(1, 0, QString("Console"))
        	self.disable_ed()
        	self.filename = ""
        

    def delete_entry(self):
        	self.table1.removeRow(self.selectedEntry[0])
        	self.table1.removeColumn(self.selectedEntry[0])
        	self.programs.pop(self.selectedEntry[0] - 2)
        	self.disable_ed()
        

    def disable_ed(self):
        	self.selectedEntry = [0,0]
        	self.deleteButton.setEnabled(0)
        	self.replaceButton.setEnabled(0)
        

    def new_graph(self):
        	for i in range(0, len(self.programs) + 2):
        		for j in range(0, len(self.programs) + 2):
        			self.table1.clearCell(i, j)
        	self.init_two()
        

    def open_command(self):
        	from commands import getoutput
        	if self.filename == "":
        		temp = QFileDialog.getOpenFileName(getoutput("echo ~"), "Commands (*.cmd);;All Files (*.*)", self, "Save as", "Choose a file").ascii()
        	else:
        		temp = QFileDialog.getOpenFileName(self.filename, "Commands (*.cmd);;All Files (*.*)", self, "Save as", "Choose a file").ascii()
        	if temp == None:
        		return
        	self.filename = temp
        	file = open(self.filename, "r")
        	command = file.read()
        	file.close()
        	
        	def add_to_graph(s):
        		self.lineEdit1.setText(s)
        		self.add_entry()
        	
        	tempstring = ""
        	mode = 1
        	for i in range(0, len(command)):
        		if command[i] == '-' and mode == 1:
        			if command[i + 1] == 'e':
        				i += 2
        				mode = 2
        		if command[i] == ":" and mode == 1:
        			i += 1
        			tempstring = ""
        			while command[i] != '"' and command[i - 1] != '\\':
        				tempstring += command[i]
        				i += 1
        			add_to_graph(tempstring)
        		if command[i] == ',' and mode == 2:
        			tempstring = ""
        			frm = 0
        			dest = 0
        			while command[i] != ' ':
        				i -= 1
        			i += 1
        			while command[i] != ',':
        				tempstring += command[i]
        				i += 1
        			i += 1
        			frm = int(tempstring)
        			tempstring = ""
        			while command[i] != " " and command[i] != "\n":
        				tempstring += command[i]
        				i += 1
        			dest = int(tempstring)
        			self.table1.setText(frm + 1, dest + 1, "X")
        

    def save_command(self):
        	if self.filename == "":
        		self.saveas_command()
        		return
        	command = "../testadj "
        	for i in range(0, len(self.programs)):
        		command += " \"%d:" % (i + 1) + self.programs[i] + "\" "
        	command += "-e "
        	for i in range(1, len(self.programs) + 1):
        		for j in range(1, len(self.programs) + 2):
        			if self.table1.text(i, j).ascii() == "X":
        				command += " %d," % i + "%d " % (j - 1)
        	file = open(self.filename, "w")
        	file.write(command)
        	file.write("\n")
        	file.close()
        

    def saveas_command(self):
        	from commands import getoutput
        	if self.filename == "":
        		temp = QFileDialog.getSaveFileName(getoutput("echo ~"), "Commands (*.cmd);;All Files (*.*)", self, "Save as", "Choose a file").ascii()
        	else:
        		temp = QFileDialog.getSaveFileName(self.filename, "Commands (*.cmd);;All Files (*.*)", self, "Save as", "Choose a file").ascii()
        	if temp != None:
        		self.filename = temp
        		self.save_command()
        

    def show_about(self):
        	from aboutbox import aboutBox
        	box = aboutBox(self, "About", 0, 0)
        	box.show()
        	box.exec_loop()	
        

    def display_config(self):
        	from configbox import configBox
        	box = configBox(self, "QTPlumb Config", 0, 0)
        	box.init_two()
        	box.show()
        	box.exec_loop()
        

    def __tr(self,s,c = None):
        return qApp.translate("Form1",s,c)
