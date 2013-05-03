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


void Form1::run_programs()
{
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
}

void Form1::table_click()
{
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
}


void Form1::add_entry()
{
	s = self.lineEdit1.text().ascii()
	self.programs.append(s)
	self.table1.setText(len(self.programs) + 1, 0, s)
	self.table1.setText(0, len(self.programs) + 1, s)
}


void Form1::replace_entry()
{
	s = self.lineEdit1.text().ascii()
	self.programs[self.selectedEntry[0] - 1] = s
	self.table1.setText(self.selectedEntry[0], 0, s)
	self.table1.setText(0, self.selectedEntry[0], s)
}

void Form1::init_two()
{
	self.programs = []
	self.table1.setText(0, 1, QString("Console"))
	self.table1.setText(1, 0, QString("Console"))
	self.disable_ed()
	self.filename = ""
}


void Form1::delete_entry()
{
	self.table1.removeRow(self.selectedEntry[0])
	self.table1.removeColumn(self.selectedEntry[0])
	self.programs.pop(self.selectedEntry[0] - 2)
	self.disable_ed()
}


void Form1::disable_ed()
{
	self.selectedEntry = [0,0]
	self.deleteButton.setEnabled(0)
	self.replaceButton.setEnabled(0)
}


void Form1::new_graph()
{
	for i in range(0, len(self.programs) + 2):
		for j in range(0, len(self.programs) + 2):
			self.table1.clearCell(i, j)
	self.init_two()
}


void Form1::open_command()
{
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
}


void Form1::save_command()
{
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
}


void Form1::saveas_command()
{
	from commands import getoutput
	if self.filename == "":
		temp = QFileDialog.getSaveFileName(getoutput("echo ~"), "Commands (*.cmd);;All Files (*.*)", self, "Save as", "Choose a file").ascii()
	else:
		temp = QFileDialog.getSaveFileName(self.filename, "Commands (*.cmd);;All Files (*.*)", self, "Save as", "Choose a file").ascii()
	if temp != None:
		self.filename = temp
		self.save_command()
}



void Form1::show_about()
{
	from aboutbox import aboutBox
	box = aboutBox(self, "About", 0, 0)
	box.show()
	box.exec_loop()	
}


void Form1::display_config()
{
	from configbox import configBox
	box = configBox(self, "QTPlumb Config", 0, 0)
	box.init_two()
	box.show()
	box.exec_loop()
}
