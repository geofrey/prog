# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutbox.ui'
#
# Created: Fri Jun 10 02:19:14 2005
#      by: The PyQt User Interface Compiler (pyuic) 3.13
#
# WARNING! All changes made in this file will be lost!


from qt import *


class aboutBox(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("aboutBox")



        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(60,70,291,231))

        self.languageChange()

        self.resize(QSize(447,388).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("About"))
        self.textLabel1.setText(self.__tr("Plumber version 0.9"))


    def __tr(self,s,c = None):
        return qApp.translate("aboutBox",s,c)
