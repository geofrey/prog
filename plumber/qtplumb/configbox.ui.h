/****************************************************************************
** ui.h extension file, included from the uic-generated form implementation.
**
** If you want to add, delete, or rename functions or slots, use
** Qt Designer to update this file, preserving your code.
**
** You should not define a constructor or destructor in this file.
** Instead, write your code in functions called init() and destroy().
** These will automatically be called by the form's constructor and
** destructor.
*****************************************************************************/


void configBox::ok_click()
{
	from commands import getoutput
	file = open(getoutput("echo ~") + "/.qtplumb", "w")
	file.write(self.plumberPath.text().ascii())
	file.write("\n")
	file.write(self.xtermPath.text().ascii())
	file.close()
	self.close()
}

void configBox::browse_plumber()
{
	location = QFileDialog.getOpenFileName(self.plumberPath.text(), "All files (*)", self, "Plumber location").ascii()
	if location != None:
		self.plumberPath.setText(QString(location))
}

void configBox::browse_xterm()
{
	location = QFileDialog.getOpenFileName(self.xtermPath.text(), "All files (*)", self, "Plumber location").ascii()
	if location != None:
		self.xtermPath.setText(QString(location))
}

void configBox::init_two()
{
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
}
