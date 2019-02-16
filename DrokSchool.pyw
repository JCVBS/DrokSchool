#!usr/bin/env python3

##########################
#                        #
#     DrokSchool v1.0    #
#                        #
#       by: JCVBS        #
#                        #
##########################

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pickle
import sys
import os

class SchoolYearsManagament():
	def __init__(self, access_user, schoolyear):
		"""docstring for SchooolYearsManagament: To record and save the data serialization is used.
			DrokSchool works on and was tested on linux(Ubuntu 18.04, linux-mint 19) and windows(windows-10)"""

		self.folder_access = access_user # "access_user" is the name of folder this class
		self.schoolyear = schoolyear
		self.root = Tk()
		self.root.title("DrokSchool")
		self.root.resizable(0, 0)
		self.database = {}
		self.tell = 0
		self.appls = {}
		self.test = True
		self.appl = ""

		if sys.platform != "linux":
			self.root.iconbitmap("database/gallery/logo.ico")

		# Variables of Controls
		self.subjectDel = StringVar()
		self.noteDel = StringVar()
		self.noteAdd = StringVar()

		# Title of the workspace
		Label(self.root, text = "DrokSchool | Workspace", font=("Comic Sans MS" ,15), fg = "#2c30ed").grid(row = 0, column = 0, sticky = W, pady = 10, padx = 12)

		# Frames
		frameSubjects = LabelFrame(self.root, text = " Subjects ", font=("Comic Sans MS" ,12), fg = "#242424")
		frameSubjects.grid(row = 1, columnspan = 2, pady = 10, padx = 10)

		# Trees: --SUBJECTS--
		self.treeMat = ttk.Treeview(frameSubjects, height = 10, selectmode = BROWSE)
		self.treeMat.grid(row = 0, column = 0)
		self.treeMat.heading("#0", text = "Mathematics", anchor = CENTER)
		self.treeMat.column("#0", width=150)

		self.treeMat.bind("<Double-1>", self.set_values)

		self.treeNat = ttk.Treeview(frameSubjects, height = 10)
		self.treeNat.grid(row = 0, column = 1)
		self.treeNat.heading("#0", text = "Natural Sciences", anchor = CENTER)
		self.treeNat.column("#0", width=150)

		self.treeNat.bind("<Double-1>", self.set_values)

		self.treeSc = ttk.Treeview(frameSubjects, height = 10)
		self.treeSc.grid(row = 0, column = 2)
		self.treeSc.heading("#0", text = "Social Studies", anchor = CENTER)
		self.treeSc.column("#0", width=150)

		self.treeSc.bind("<Double-1>", self.set_values)

		self.treeL = ttk.Treeview(frameSubjects, height = 10)
		self.treeL.grid(row = 0, column = 3)
		self.treeL.heading("#0", text = "Language", anchor = CENTER)
		self.treeL.column("#0", width=150)

		self.treeL.bind("<Double-1>", self.set_values)

		self.treeEn = ttk.Treeview(frameSubjects, height = 10)
		self.treeEn.grid(row = 0, column = 4)
		self.treeEn.heading("#0", text = "English", anchor = CENTER)
		self.treeEn.column("#0", width=150)

		self.treeEn.bind("<Double-1>", self.set_values)

		self.treePy = ttk.Treeview(frameSubjects, height = 10)
		self.treePy.grid(row = 0, column = 5)
		self.treePy.heading("#0", text = "Physical Education", anchor = CENTER)
		self.treePy.column("#0", width=160)

		self.treePy.bind("<Double-1>", self.set_values)

		self.treeEs = ttk.Treeview(frameSubjects, height = 10)
		self.treeEs.grid(row = 0, column = 6)
		self.treeEs.heading("#0", text = "Esthetic Culture", anchor = CENTER)
		self.treeEs.column("#0", width=160)

		self.treeEs.bind("<Double-1>", self.set_values)

		self.treeAssi = ttk.Treeview(frameSubjects, height = 10)
		self.treeAssi.grid(row = 0, column = 7,)
		self.treeAssi.heading("#0", text = "Assistance", anchor = CENTER)
		self.treeAssi.column("#0", width = 150)

		self.treeAssi.bind("<Double-1>", self.set_values)

		# { MENU }
		frameMenu = LabelFrame(self.root, text = " Menu | Options ", font=("Comic Sans MS" ,12), fg = "#2c30ed")
		frameMenu.grid(row = 2, column = 0, pady = 10, padx = 10, sticky = W)

		# { OPTIONS-STUDENTS }
		frameStudents = LabelFrame(frameMenu, text = " Options ", fg = "#242424")
		frameStudents.grid(row = 0, column = 0, pady = 10, padx = 10, sticky = N + S)

		# Buttons
		if sys.platform != "linux":
			Button(frameStudents, text = "Options of Students", command = self.options_students).grid(row = 0, column = 0, sticky = W + E, pady = 4, padx = 5)
			Button(frameStudents, text = "Create Student", command = self.create_students).grid(row = 1, column = 0, sticky = W +E, pady = 4, padx = 5)
			Button(frameStudents, text = "Calculate Average", command = self.calculate_average).grid(row = 2, column = 0, sticky = W +E, pady = 4, padx = 5)
		else:
			Button(frameStudents, text = "Options of Students", command = self.options_students).grid(row = 0, column = 0, sticky = W + E, pady = 2, padx = 5)
			Button(frameStudents, text = "Create Student", command = self.create_students).grid(row = 1, column = 0, sticky = W +E, pady = 2, padx = 5)
			Button(frameStudents, text = "Calculate Average", command = self.calculate_average).grid(row = 2, column = 0, sticky = W +E, pady = 2, padx = 5)

		# { OPTIONS-STUDENTS }
		frameOptions = LabelFrame(frameMenu, text = " Students Options ", fg = "#242424")
		frameOptions.grid(row = 0, column = 1, pady = 10, padx = 10, sticky = W)

		# Options of Add
		frameAdd = LabelFrame(frameOptions)
		frameAdd.grid(row = 0, column = 0, pady = 11, padx = 10)

		Label(frameAdd, text = "Subject:").grid(row = 0, column = 0, padx = 5, pady = 2)

		# Combo
		self.combo = ttk.Combobox(frameAdd, state = "disable", width = 19, justify = CENTER)
		self.combo["values"] = ["Mathematics", "Natural Sciences", "Social Studies", "Language", "English", "Physical Education", "Esthetic Culture", "Assistance"]
		self.combo.grid(row = 0, column = 1, padx = 5, pady = 2)

		self.combo.bind("<<ComboboxSelected>>", self.combo_selection)

		Label(frameAdd, text = "New note:").grid(row = 1, column = 0, padx = 5)
		self.note = Entry(frameAdd, justify = CENTER, textvariable = self.noteAdd, state = "readonly")
		self.note.grid(row = 1, column = 1, padx = 5)

		Button(frameAdd, text = "Add Note", command = self.add_notes).grid(row = 2, columnspan = 2, sticky = W + E)

		# Optiosn of delete
		frameDel = LabelFrame(frameOptions)
		frameDel.grid(row = 0, column = 1, pady = 11, padx = 10)

		Label(frameDel, text = "Subject:").grid(row = 0, column = 0, padx = 5, pady = 2)
		Entry(frameDel, justify = CENTER, state = "readonly", textvariable = self.subjectDel).grid(row = 0, column = 1, padx = 5, pady = 2)

		Label(frameDel, text = "Note:").grid(row = 1, column = 0, padx = 5)
		Entry(frameDel, justify = CENTER, state = "readonly", textvariable = self.noteDel).grid(row = 1, column = 1, padx = 5)

		Button(frameDel, text = "Delete Note", command = self.delete_notes).grid(row = 2, columnspan = 2, sticky = W + E)

		# Selection Students
		frame = LabelFrame(frameOptions)
		frame.grid(row = 0, column = 2, pady = 10, padx = 10)

		self.treeAppl = ttk.Treeview(frame, height = 3)
		self.treeAppl.grid(row = 0, column = 1)

		self.treeAppl.heading("#0", text = "Students", anchor = CENTER)
		self.treeAppl.column("#0", minwidth = 10, width = 170)

		self.treeAppl.bind("<Double-1>", self.setSubjects)

		self.students_load()
		self.root.mainloop()

	def combo_selection(self, event):
		self.note["state"] = "normal"

	def generate_report(self, data_report):
		window_report = Toplevel()
		window_report.resizable(0, 0)

		# Variable of Control
		report_route = StringVar()

		if sys.platform != "linux":
			window_report.iconbitmap("database/gallery/logo.ico")

		frame = LabelFrame(window_report, text = " Generate Report ", fg = "#2c30ed", font=("Comic Sans MS" , 12))
		frame.grid(row = 0, column = 0, pady = 5, padx = 10)

		frameInf = LabelFrame(window_report, text = " Information ", fg = "#2c30ed")
		frameInf.grid(row = 1, column = 0, pady = 5, padx = 10)

		# Report Input
		Label(frame, text = "Report of the route:", fg = "#242424").grid(row = 0, column = 0, pady = 5, padx = 5)
		Entry(frame, justify = CENTER, textvariable = report_route).grid(row = 0, column = 1, pady = 5, padx = 5)

		# Information for the user
		Example = "\n\nIn Linux: /home/user/Desktop\n" + r"In Windows: C:\Users\user01\Desktop"
		Inf = Label(frameInf, text = "Enter the route where the report will be created\nThe route must be complete, Example:" + Example)
		Inf.grid(row = 0, column = 0, pady = 5, padx = 5)

		report = """

		-Average:

			-Mathematics-------------[{[0]}]
			-Natural Sciences--------[{[1]}]
			-Social Studies----------[{[2]}]
			-Language----------------[{[3]}]
			-English-----------------[{[4]}]
			-Physical Education------[{[5]}]
			-Esthetic Culture--------[{[6]}]
			________________________________

			-Total Average-----------[{[7]}]

			""".format(data_report, data_report, data_report, data_report,
				data_report, data_report, data_report, data_report)

		def set_report():
			os.chdir("/")
			try:
				with open(report_route.get() + "/report " + self.appl + ".txt", "w") as report_file:
					report_file.write(report)

				messagebox.showinfo("Information", "The report has been successfully generated")
				window_report.destroy()

			except:
				try:
					with open(report_route.get() + "report " + self.appl + ".txt", "w") as report_file:
						report_file.write(report)

					messagebox.showinfo("Information", "The report has been successfully generated")
					window_report.destroy()

				except:
					try:
						with open(report_route.get() + r"\report " + self.appl + ".txt", "w") as report_file:
							report_file.write(report)

						messagebox.showinfo("Information", "The report has been successfully generated")
						window_report.destroy()

					except:
						messagebox.showwarning("File Not Found Error", "The route is incorrect or there was a character error, try again...")
						report_route.set("")

		Button(frame, text = "Generate report", command = lambda:set_report()).grid(row = 1, columnspan = 2, sticky = W + E)

	def calculate_average(self):
		if self.appl != "":
			check = 0
			subjects = dict(self.database[self.appl].items())
			for subject, notes in subjects.items():
				if subject != "Assistance":
					if len(notes) >= 2:
						check += 1

			if check == 7:
				window = Toplevel()
				window.resizable(False, False)

				if sys.platform != "linux":
					window.iconbitmap("database/gallery/logo.ico")

				# Frame
				frame = LabelFrame(window, text = " Average ", font=("Comic Sans MS" ,13), fg = "#2c30ed")
				frame.grid(row = 0, column = 0, pady = 10, padx = 10)

				# Set Labels-Subjects

				tell = 0
				for subject in subjects.keys():
					Label(frame, text = subject + ":").grid(row = tell, column = 0, sticky = W, padx = 5, pady = 5)
					tell += 1

				# Calculates the Average of the Subjects

				try:
					with open("database/schoolyears/" + self.folder_access + "/" + self.schoolyear, "rb") as file:
						self.database = pickle.load(file)
				except:
					pass

				data_report = []
				averages = []
				tell = 0

				for subject, notes in subjects.items():
					if subject != "Assistance":
						tellnot = 0
						totalNote = 0
						for note in notes:
							tellnot += 1
							totalNote += note

						average = round((totalNote / tellnot), 2)
						averages.append(average)
						data_report.append(average)
						Label(frame, text = "[ " + str(average) + " ]").grid(row = tell, column = 1, padx = 5, pady = 5)
						tell += 1

				tell = 0
				total_average = 0

				# Calculate the total Average
				for average in averages:
					tell += 1
					total_average += average

				total_average = round(total_average / tell, 2)
				data_report.append(total_average)

				# Separator
				if sys.platform != "linux":
					Label(frame, text =  "─────────────").grid(row = 7, columnspan = 2)
				else:
					Label(frame, text =  "───────────────────────").grid(row = 7, columnspan = 2)

				# Set Total Average
				Label(frame, text = "Total Average:").grid(row = 8, column = 0, padx = 5, pady = 3, sticky = W)
				Label(frame, text = "[ " + str(total_average) + " ]", fg = "#2c30ed").grid(row = 8, column = 1, padx = 5, pady = 3)


				Button(frame, text = "Generate report", command = lambda:self.generate_report(data_report)).grid(row = 9, columnspan = 2, sticky = W + E)

	def set_values(self, event):
		for tree in (self.treeMat, self.treeNat, self.treeSc, self.treeL, self.treeEn, self.treePy, self.treeEs, self.treeAssi):
			try:
				if len(tree.item(tree.selection()[0], "values")) > 1:
					subject = tree.item(tree.selection()[0], "values")[0] + " " + tree.item(tree.selection()[0], "values")[1]

					self.subjectDel.set(subject)
					self.noteDel.set(tree.item(tree.selection()[0], "text"))
				else:
					self.subjectDel.set(tree.item(tree.selection()[0], "values")[0])
					self.noteDel.set(tree.item(tree.selection()[0], "text"))
			except:
				pass

		self.setSubjects(0)

	def students_load(self):
		try:
			with open("database/schoolyears/" + self.folder_access + "/" + self.schoolyear, "rb") as file:
				self.database = pickle.load(file)
		except:
			pass

		for appl in self.treeAppl.get_children():
			self.treeAppl.delete(appl)

		for appl in self.database.keys():
			self.treeAppl.insert("", 0, text = appl)

	def add_notes(self):
		if self.appl != "" and self.combo.get() != "" and self.noteAdd.get() != "":
			try:
				subjects_update = dict(self.database[self.appl].items())
				subjects_update[self.combo.get()].append(int(self.noteAdd.get()))

				self.database[self.appl] = subjects_update
				with open("database/schoolyears/" + self.folder_access + "/" + self.schoolyear, "wb") as file:
					pickle.dump(self.database, file)

				self.setSubjects(0)
				self.combo.set("")
				self.noteAdd.set("")

			except:
				pass

	def delete_notes(self):
		if self.appl != "" and self.subjectDel.get() != "" and self.noteDel.get() != "":
			subjects_update = dict(self.database[self.appl].items())
			subjects_update[self.subjectDel.get()].remove(int(self.noteDel.get()))

			self.database[self.appl] = subjects_update
			with open("database/schoolyears/" + self.folder_access + "/" + self.schoolyear, "wb") as file:
					pickle.dump(self.database, file)

			self.setSubjects(0)
			self.subjectDel.set("")
			self.noteDel.set("")

	def setSubjects(self, event):
		try:
			with open("database/schoolyears/" + self.folder_access + "/" + self.schoolyear, "rb") as file:
				self.database = pickle.load(file)

			self.database.items()

			self.combo["state"] = "readonly"

			appleCore = self.treeAppl.item(self.treeAppl.selection()[0], "text")
			self.appl = appleCore

			for appl, notes in self.database[appleCore].items():
				if appl == "Mathematics":
					for note in self.treeMat.get_children():
						self.treeMat.delete(note)
					for note in notes:
						self.treeMat.insert("", 0, text = note, values = "Mathematics")

				elif appl == "Natural Sciences":
					for note in self.treeNat.get_children():
						self.treeNat.delete(note)
					for note in notes:
						self.treeNat.insert("", 0, text = note, values = "Natural Sciences")

				elif appl == "Social Studies":
					for note in self.treeSc.get_children():
						self.treeSc.delete(note)
					for note in notes:
						self.treeSc.insert("", 0, text = note, values = "Social Studies")

				elif appl == "Language":
					for note in self.treeL.get_children():
						self.treeL.delete(note)
					for note in notes:
						self.treeL.insert("", 0, text = note, values = "Language")

				elif appl == "English":
					for note in self.treeEn.get_children():
						self.treeEn.delete(note)
					for note in notes:
						self.treeEn.insert("", 0, text = note, values = "English")

				elif appl == "Physical Education":
					for note in self.treePy.get_children():
						self.treePy.delete(note)
					for note in notes:
						self.treePy.insert("", 0, text = note, values = "Physical Education")

				elif appl == "Esthetic Culture":
					for note in self.treeEs.get_children():
						self.treeEs.delete(note)
					for note in notes:
						self.treeEs.insert("", 0, text = note, values = "Esthetic Culture")

				else:
					for note in self.treeAssi.get_children():
						self.treeAssi.delete(note)
					for note in notes:
						self.treeAssi.insert("", 0, text = note, values = "Assistance")
		except:
			pass

	def create_students(self):
		window = Toplevel()
		window.resizable(False, False)

		if sys.platform != "linux":
			window.iconbitmap("database/gallery/logo.ico")

		# Variable of control
		student = StringVar()

		# Frames
		frame = LabelFrame(window, text = " Create Student ", font=("Comic Sans MS" ,12), fg = "#2c30ed")
		frame.grid(row = 0, column = 0, pady = 10, padx = 10)

		# Input Student
		Label(frame, text = "Name-Student:").grid(row = 0, column = 0, pady = 7, padx = 4)
		name = Entry(frame, textvariable = student, justify = CENTER).grid(row = 0, column = 1, pady = 7, padx = 4)

		def create(name_Student):
			try:
				with open("database/schoolyears/" + self.folder_access + "/" + self.schoolyear, "rb") as file:
					self.database = pickle.load(file)
			except:
				pass

			if name_Student != "":
				self.database[name_Student] = {

					"Mathematics": [],
					"Natural Sciences": [],
					"Social Studies": [],
					"Language": [],
					"English": [],
					"Physical Education": [],
					"Esthetic Culture": [],
					"Assistance": []

				}

				with open("database/schoolyears/" + self.folder_access + "/" + self.schoolyear, "wb") as file:
					pickle.dump(self.database, file)

				window.destroy()
				self.students_load()
			else:
				pass

		Button(frame, text = "Add Student", command = lambda:create(student.get())).grid(row = 2, column = 0, columnspan = 2, sticky = W + E)

	def options_students(self):
		try:
			with open("database/schoolyears/" + self.folder_access + "/" + self.schoolyear, "rb") as file:
				self.database = pickle.load(file)

			self.database.items() # we check if there are students

			window = Toplevel()
			window.resizable(False, False)

			if sys.platform != "linux":
				window.iconbitmap("database/gallery/logo.ico")

			# Variables of Control
			student = StringVar()
			name_student = StringVar()

			# Frames
			frameSelect = LabelFrame(window)
			frameSelect.grid(row = 0, column = 0, pady = 10, padx = 10, sticky = S)

			frameOptions = LabelFrame(window, text = "Options", font=("Comic Sans MS" ,12), fg = "#2c30ed")
			frameOptions.grid(row = 0, column = 1, pady = 10, padx = 8, sticky = N + S)

			frameEdit = LabelFrame(frameOptions, text = " Options Edit ", font=("Comic Sans MS" ,12), fg = "#2c30ed")
			frameEdit.grid(row = 0, column = 0, pady = 9, padx = 9)

			frameDelete = LabelFrame(frameOptions, text = "Options Delete ", font=("Comic Sans MS" ,12), fg = "#2c30ed")
			frameDelete.grid(row = 1, column = 0, pady = 9, padx = 9)

			def OnDoubleClick(event):
				try:
					item = self.tree.selection()[0]
					student.set(self.tree.item(item, "text"))
					new_student["state"] = "normal"
				except:
					pass

			def getData():
				self.tree = ttk.Treeview(frameSelect, height = 11)
				self.tree.grid(row = 0, column = 0)
				self.tree.heading("#0", text = "Students", anchor = CENTER)

				for element in self.tree.get_children():
					self.tree.delete(element)

				for appl in self.database.keys():
					self.tree.insert("", "end", text = appl)

				self.tree.bind("<Double-1>", OnDoubleClick)

			def edit_student():
				self.database[new_student.get()] = self.database[student.get()]
				del(self.database[student.get()])

				with open("database/schoolyears/" + self.folder_access + "/" + self.schoolyear, "wb") as file:
					pickle.dump(self.database, file)

				student.set("")
				name_student.set("")
				new_student["state"] = "readonly"
				getData()
				self.students_load()

			Label(frameEdit, text = "Name of Student:").grid(row = 0, column = 0, padx = 5, sticky = W)
			Entry(frameEdit, state = "readonly", justify = CENTER, textvariable = student).grid(row = 0, column = 1, padx = 5)

			Label(frameEdit, text = "New name Student:").grid(row = 1, column = 0, padx = 5, sticky = W)
			new_student = Entry(frameEdit, state = "readonly", justify = CENTER, textvariable = name_student)
			new_student.grid(row = 1, column = 1, padx = 5)

			Button(frameEdit, text = "Add update", command = lambda:edit_student()).grid(row = 2, columnspan = 2, sticky = W + E)

			def delete_student():
				del(self.database[student.get()])

				with open("database/schoolyears/" + self.folder_access + "/" + self.schoolyear, "wb") as file:
					pickle.dump(self.database, file)

				student.set("")
				new_student["state"] = "readonly"
				getData()
				self.students_load()

			Label(frameDelete, text = "Student:").grid(row = 0, column = 0, padx = 5)
			Entry(frameDelete, state = "readonly", justify = CENTER, textvariable = student, width = 29).grid(row = 0, column = 1, padx = 5)

			Button(frameDelete, text = "Delete", command = lambda:delete_student()).grid(row = 1, columnspan = 2, sticky = W + E)

			Button(frameSelect, text = "Exit", command = lambda:window.destroy()).grid(row = 2, column = 0, sticky = W + E)
			getData()

		except:
			pass

class AccessManagement():
	def __init__(self):
		self.accounts_database = {}
		self.root = Tk()
		self.root.title("DrokSchool Login")
		self.list_schoolyears = []
		self.root.resizable(0,0)

		if sys.platform != "linux":
			self.root.iconbitmap("database/gallery/logo.ico")

		# Variables of Controls
		self.usr = StringVar()
		self.clv = StringVar()

		# Title
		Label(self.root, text = "DrokSchool Login", font=("Comic Sans MS", 15), fg = "#2c30ed").grid(row = 0, column = 0, pady = 10 , padx = 10, sticky = W)

		# Login Frame
		frameLogin = LabelFrame(self.root, text = " Login ", font=("Comic Sans MS" ,12), fg = "#242424")
		frameLogin.grid(row = 1, column = 0, padx = 10)

		# User input
		Label(frameLogin, text = "user:").grid(row = 0, column = 0, padx = 5)
		self.user = Entry(frameLogin)
		self.user.grid(row = 0, column = 1, padx = 5)

		# Password input
		Label(frameLogin, text = "pass:").grid(row = 1, column = 0, padx = 5)
		self.password = Entry(frameLogin, show = "*")
		self.password.grid(row = 1, column = 1, padx = 5)

		# Button Access
		Button(frameLogin, text = "To access", command = self.login).grid(row = 2, columnspan = 2, sticky = W + E)

		#-----------------------------------------------------------------------------------------------------------|

		# Register Frame
		frameRegister = LabelFrame(self.root, text = " Register ", font=("Comic Sans MS" ,12), fg = "#242424")
		frameRegister.grid(row = 1, column = 1, padx = 10)

		# User input
		Label(frameRegister, text = "user:").grid(row = 0, column = 0, padx = 5)
		self.userReg = Entry(frameRegister, textvariable = self.usr)
		self.userReg.grid(row = 0, column = 1, padx = 5)

		# Password input
		Label(frameRegister, text = "pass:").grid(row = 1, column = 0, padx = 5)
		self.passwordReg = Entry(frameRegister, show = "*", textvariable = self.clv)
		self.passwordReg.grid(row = 1, column = 1, padx = 5)

		# Button
		Button(frameRegister, text = "Check in", command = self.register).grid(row = 2, columnspan = 2, sticky = W + E)

		# Message
		self.menssage = Label(self.root, text = "")
		self.menssage.grid(row = 2, column = 0, pady = 7, padx = 5)

		self.root.mainloop()

	def login(self):
		try:
			with open("database/accounts_database", "rb") as file:
				self.accounts_database = pickle.load(file)

			self.accounts_database.items()

			if len(self.user.get()) != 0 and len(self.password.get()) != 0:
				if self.user.get() not in self.accounts_database.keys():
					self.menssage.grid(row = 2, column = 0)
					self.menssage["text"] = "[ The account does not exist ]"
				else:
					if self.accounts_database[self.user.get()] == self.password.get():
						user = self.user.get()
						self.root.destroy()
						self.schoolyears_managament(user)
					else:
						self.menssage.grid(row = 2, column = 0)
						self.menssage["text"] = "[ Password incorrect, try again... ]"
			else:
				self.menssage.grid(row = 2, column = 0)
				self.menssage["text"] = "[ Error, try again... ]"
		except:
			self.menssage.grid(row = 2, column = 0)
			self.menssage["text"] = "[ The account does not exist ]"

	def register(self):
		try:
			with open("database/accounts_database", "rb") as file:
				self.accounts_database = pickle.load(file)
		except:
			pass

		if len(self.userReg.get()) != 0 and len(self.passwordReg.get()) != 0:
			if self.userReg.get() not in self.accounts_database.keys():
				self.accounts_database[self.userReg.get()] = self.passwordReg.get()

				with open("database/accounts_database", "wb") as file:
					pickle.dump(self.accounts_database, file)

				self.menssage.grid(row = 2, column = 1)
				self.menssage["text"] = "[ Has been registered correctly ]"

				self.usr.set("")
				self.clv.set("")
			else:
				self.menssage.grid(row = 2, column = 1)
				self.menssage["text"] = "[ Username not available ]"
		else:
			self.menssage.grid(row = 2, column = 1)
			self.menssage["text"] = "[ User and password is required ]"

	def schoolyears_managament(self, access_user): # "access_user" is for the name of the folder in this method
		window_access = Tk()
		window_access.title("School years Access")
		window_access.resizable(False, False)

		if sys.platform != "linux":
			window_access.iconbitmap("database/gallery/logo.ico")

		# Variables of Controls
		self.name_schoolyear = StringVar()
		self.schoolyear_select = StringVar()
		self.name_edit = StringVar()

		# Title
		Label(window_access, text = "School year Options", font=("Comic Sans MS" ,15), fg = "#2c30ed").grid(row = 0, column = 0, pady = 10, padx = 10, sticky = W)

		# Frames
		frame = LabelFrame(window_access)
		frame.grid(row = 1, column = 1, pady = 10, padx = 5, sticky = N + S)

		workFrame = LabelFrame(window_access)
		workFrame.grid(row = 1, column = 0, pady = 10, padx = 5, sticky = N + S)

		createFrame = LabelFrame(frame, text = " Create School year ", fg = "#2c30ed")
		createFrame.grid(row = 1, column = 0, pady = 10, padx = 5)

		deleteFrame = LabelFrame(frame, text = " Delete School year ", fg = "#2c30ed")
		deleteFrame.grid(row = 2, column = 0, pady = 10, padx = 5)

		editFrame = LabelFrame(frame, text = " Edit School year ", fg = "#2c30ed")
		editFrame.grid(row = 3, column = 0, pady = 10, padx = 5)

		# Tree
		tree = ttk.Treeview(workFrame, height = 14)
		tree.grid(row = 0, column = 0, sticky = W)
		tree.heading("#0", text = "School years", anchor = CENTER)

		def schoolyears_access():
			try:
				selected = tree.selection()[0]
				schoolyear = tree.item(selected, "text")
				window_access.destroy()
				SchoolYearsManagament(access_user, schoolyear)
				
			except:
				pass

		# Access Button
		Button(workFrame, text = "To access", command = lambda:schoolyears_access()).grid(row = 1, column = 0, sticky = W + E)

		def set_schoolyears(event):
			try:
				schoolyear = tree.selection()[0]
				self.schoolyear_select.set(tree.item(schoolyear, "text"))
				self.entry_name_new["state"] = "normal"

			except:
				pass

		def get_schoolyears():
			try:
				with open("database/schoolyears" + "/" + access_user + "/list_schoolyears", "rb") as list_schoolyears:
					self.list_schoolyears = pickle.load(list_schoolyears)
			except:
				pass

			for schoolyear in tree.get_children():
				tree.delete(schoolyear)

			for schoolyear in self.list_schoolyears:
				tree.insert("", 0, text = schoolyear)

			tree.bind("<Double-1>", set_schoolyears)

		def register_schoolyear():
			if len(self.name_schoolyear.get()) != 0:
				try:
					os.mkdir("database/schoolyears/" + access_user )

				except FileExistsError:
					try:
						file = open("database/schoolyears" + "/" + access_user + "/list_schoolyears", "rb")
						self.list_schoolyears = pickle.load(file)
						file.close()

					except FileNotFoundError:
						pass

				file = open("database/schoolyears" + "/" + access_user + "/list_schoolyears", "wb")

				self.list_schoolyears.append(self.name_schoolyear.get())

				pickle.dump(self.list_schoolyears, file)
				file.close()

				self.name_schoolyear.set("")

				get_schoolyears()

		def delete_schoolyear():
			if len(self.schoolyear_select.get()) != 0:
				self.list_schoolyears.remove(self.schoolyear_select.get())
				with open("database/schoolyears" + "/" + access_user + "/list_schoolyears", "wb") as list_schoolyears:
					pickle.dump(self.list_schoolyears, list_schoolyears)

				try:
					os.remove("database/schoolyears/" + access_user + "/" + self.schoolyear_select.get())
				except:
					pass

				self.schoolyear_select.set("")
				self.entry_name_new["state"] = "readonly"
				get_schoolyears()

		def edit_schoolyear():
			if len(self.name_edit.get()) != 0 and len(self.schoolyear_select.get()) != 0:
				with open("database/schoolyears" + "/" + access_user + "/list_schoolyears", "wb") as list_schoolyears:
					self.list_schoolyears.remove(self.schoolyear_select.get())
					self.list_schoolyears.append(self.name_edit.get())
					pickle.dump(self.list_schoolyears, list_schoolyears)

				try:
					os.rename("database/schoolyears/" + access_user + "/" + self.schoolyear_select.get(),
					 			"database/schoolyears/" + access_user + "/" + self.name_edit.get())
				except:
					pass

				self.schoolyear_select.set("")
				self.name_edit.set("")
				self.entry_name_new["state"] = "readonly"
				get_schoolyears()
 
		# Options of Create
		Label(createFrame, text = "School year:").grid(row = 0, column = 0, pady = 3, padx = 5)
		Entry(createFrame, justify = CENTER, textvariable = self.name_schoolyear, width = 24).grid(row = 0, column = 1, pady = 3, padx = 5)

		Button(createFrame, text = "Create", command = lambda:register_schoolyear()).grid(row = 1, columnspan = 2, sticky = W + E)

		# Optios of Delete
		Label(deleteFrame, text = "School year:").grid(row = 0, column = 0, pady = 3, padx = 5)
		Entry(deleteFrame, justify = CENTER, state = "readonly", textvariable = self.schoolyear_select, width = 24).grid(row = 0, column = 1, pady = 3, padx = 5)

		Button(deleteFrame, text = "Delete", command = lambda:delete_schoolyear()).grid(row = 1, columnspan = 2, sticky = W + E)

		# Options of Edit
		Label(editFrame, text = "Old school year:").grid(row = 0, column = 0, pady = 3, padx = 5, sticky = W)
		Entry(editFrame, justify = CENTER, textvariable = self.schoolyear_select, state = "readonly").grid(row = 0, column = 1, pady = 2, padx = 5)

		Label(editFrame, text = "New school year:").grid(row = 1, column = 0, pady = 3, padx = 5, sticky = W)
		self.entry_name_new = Entry(editFrame, justify = CENTER, state = "readonly", textvariable = self.name_edit)
		self.entry_name_new.grid(row = 1, column = 1, pady = 2, padx = 5)

		Button(editFrame, text = "Add update", command = lambda:edit_schoolyear()).grid(row = 2, columnspan = 2, sticky = W + E)

		get_schoolyears()

		window_access.mainloop()

if __name__ == '__main__':
	initialize = AccessManagement()