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

void Form1::additem1() {

	e = self.lineEdit1.text().ascii()
	if len(e) > 0:
		self.listBox1.insertItem(e)
		self.lineEdit1.clear()
}


void Form1::removeselection1()
{
	self.listBox1.removeItem(self.listBox1.index(self.listBox1.selectedItem()))
}


void Form1::additem2()
{
	e = self.lineEdit2.text().ascii()
	if len(e) > 0:
		self.listBox3.insertItem(e)
		self.lineEdit2.clear()
}


void Form1::removeselection2()
{
	self.listBox3.removeItem(self.listBox3.index(self.listBox3.selectedItem()))
}


void Form1::run()
{
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
}


