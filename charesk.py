#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
GUI for Charat RP, coded by Addy
"""

import Tkinter as tk
import ttk
import tkFont

import requests
import json

import threading

class MainWin(tk.Frame):
  
	def __init__(self, parent_frame):

		tk.Frame.__init__(self, parent_frame, background="#ccffcc")   
		self.parent_frame = parent_frame

		self.notebook = ttk.Notebook(self, padding=0)
		
		#Fonts
		self.courier30 = tkFont.Font(family="Courier New", size="30")
		self.courier20 = tkFont.Font(family="Courier New", size="20")
		self.courier10 = tkFont.Font(family="Courier New", size="10")
		
		
		#Variables
		
		self.main_frame = None
		
		self.user_var = None
		self.user_entry = None
		self.user_clicked = False
		
		self.alias_var = None
		self.alias_entry = None
		self.alias_clicked = False
		
		self.color_var = None
		self.color_entry = None
		self.color_clicked = False
		
		self.typing_error = None
		
		self.typat_visible = False
		
		
		self.initUI()
	
	def initUI(self):

		#Main window
		self.resize(self.parent_frame, 0, 0)
		self.parent_frame.title("Charat")
		self.resize(self, 0, 0)
		self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
		
		#Notebook
		self.resize(self.notebook, 0, 0)
		self.notebook.grid(sticky=tk.N+tk.S+tk.E+tk.W)
		
		#Main tab
		main_tab = tk.Frame(self.notebook, bg="#CCFFCC")
		self.resize(main_tab, 0, 0)
		self.notebook.add(main_tab, text="Home")
		
		#Main frame
		self.main_frame = tk.Frame(main_tab, bg="#CCFFCC")
		self.resize(self.main_frame, 0, 0)
		self.resize(self.main_frame, 2, 1)
		self.resize(self.main_frame, 2, 2)
		self.resize(self.main_frame, 2, 3)
		self.resize(self.main_frame, 1, 6)
		self.main_frame.grid(sticky=tk.N+tk.S+tk.E+tk.W)
		
		#Title
		tk.Message(self.main_frame, text="Charesk", width=300, bg="#CCFFCC", font=self.courier30).grid(row=0, column=1, 
		columnspan=2)
		
		#Username entry
		self.user_var = tk.StringVar(self.main_frame)
		self.user_entry = tk.Entry(self.main_frame, fg="gray", textvariable=self.user_var)
		self.user_entry.bind("<Button-1>", lambda event, entry=self.user_entry, clicked=self.user_clicked: self.entry_text(entry, clicked))
		self.user_entry.insert(0, "Username")
		self.user_entry.grid(row=1, column=1, sticky=tk.E, pady=10)
		
		#Alias entry
		self.alias_var = tk.StringVar(self.main_frame)
		self.alias_entry = tk.Entry(self.main_frame, fg="gray", textvariable=self.alias_var, width=10)
		self.alias_entry.bind("<Button-1>", lambda event, entry=self.alias_entry, clicked=self.alias_clicked: self.entry_text(entry, clicked))
		self.alias_entry.insert(0, "Alias")
		self.alias_entry.grid(row=1, column=2, sticky=tk.W, pady=10)
		
		#Color entry
		self.color_var = tk.StringVar(self.main_frame)
		self.color_entry = tk.Entry(self.main_frame, fg="grey", textvariable=self.color_var)
		self.color_entry.bind("<Button-1>", lambda event, entry=self.color_entry, clicked=self.color_clicked: self.entry_text(entry, clicked))
		self.color_entry.insert(0, "Color (e.g., #000000)")
		self.color_entry.grid(row=3, column=1, sticky=tk.E, pady=10)
	
		#Typing patterns button
		chat_b = tk.Button(self.main_frame, relief=tk.GROOVE, text="Typing Patterns", width=30, bg="#CCFFCC", command=self.init_typing_patterns)
		chat_b.grid(row=4, column=1, columnspan=2, padx=20, pady=20)
		
		#Group chat name entry
		url_var = tk.StringVar(self.main_frame)
		url_entry = tk.Entry(self.main_frame, textvariable=url_var)
		url_entry.grid(row=6, column=1, columnspan=2, padx=10, pady=10)
		
		#Start chatting button
		chat_b = tk.Button(self.main_frame, relief=tk.GROOVE, text="Start Chatting", bg="#CCFFCC", 
		command=lambda: self.init_chat(url_var.get()))
		chat_b.grid(row=7, column=1, columnspan=2, sticky=tk.N, padx=10, pady=10)
		
	def resize(self, widget, rowcol, num):
		#Sets specified rows and columns to be resizable; uses less code than doing it manually
		if rowcol == 1:
			widget.rowconfigure(num, weight=1)
		elif rowcol == 2:
			widget.columnconfigure(num, weight=1)
		else:
			widget.rowconfigure(num, weight=1)
			widget.columnconfigure(num, weight=1)

	def init_typing_patterns(self):
		#Displays the typing patterns when button is pressed
		if self.typat_visible == True:
			self.typing_error.grid_remove()
			self.typat_visible = False
		else:
			self.typing_error = tk.Message(self.main_frame, text="Typing patterns will go here someday ;-;", width=300, bg="#CCFFCC", font=self.courier10)
			self.typing_error.grid(row=5, column=1, columnspan=2, padx=5,pady=5)
			self.typat_visible = True
	
	def entry_text(self, entry, clicked):
		#Erases the grey explanation text in an entry when it is clicked
		if clicked == False:
			entry.delete(0, tk.END)
			entry.config(fg="black")
			clicked == True
	
	def add_window(self):
		#Placeholder for if we ever need pop-up windows
		top = tk.Toplevel()
		top.title("U R CHATTIN W SOME RANDOM DUNKASS")
		tk.Message(top, text="dunkass: wazzup").pack()
		
	def init_chat(self, url):
		#Creates a new chatting tab
		if url != "":
			NewTab(self, url)
		else:
			pass
		

class NewTab(object):
	
	def __init__(self, parent, url):
		
			self.url = url
			self.parent = parent
			
			self.tab = tk.Frame(self.parent.notebook, bg="#CCFFCC")
			self.parent.notebook.add(self.tab, text=url)
		
			self.main_frame = tk.Frame(self.tab, bg="#CCFFCC")
			self.side_frame = tk.Frame(self.tab, bg="#CCFFCC")
			
			self.message_var = tk.StringVar(self.main_frame)
			self.message_entry = None
		
			self.initUI()
			
			threading.Thread(target = self.display_messages).start()
		
	def initUI(self):
		
		self.tab.lift()
		
		self.resize(self.tab, 0, 0)

		self.resize(self.main_frame, 0, 1)
		self.resize(self.main_frame, 2, 0)
		self.resize(self.main_frame, 2, 1)
		
		self.main_frame.grid(row=0, column=0,sticky=tk.N+tk.S+tk.E+tk.W)

		#tk.Message(self.main_frame, font=self.parent.courier10, text=self.url, bg="#CCFFCC", width=300).grid(row=0, sticky=tk.N+tk.W)
		
		self.message_area = tk.Text(self.main_frame, font=self.parent.courier10)
		self.message_area.grid(row=1, columnspan=2, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
		
		#self.message_area.insert(tk.END, "Person 1 [Person1] joined chat.\nPerson 2 [Person2] joined chat.\nPerson1: hi\nPerson1: whats up")
		
		self.message_area.config(state=tk.DISABLED)
		
		self.message_var = tk.StringVar(self.main_frame)
		self.message_entry = tk.Entry(self.main_frame, textvariable=self.message_var)
		#self.message_entry.bind("<Return>", self.send_message)
		self.message_entry.grid(row=2, column=0, columnspan=2, sticky=tk.S+tk.E+tk.W, padx=5, pady=5)
		
		#	enter_button = tk.Button(self.main_frame, text="Send", command=lambda: self.send_message(message_var.get()))
		#	enter_button.grid(row=2, column=1, padx=5, pady=5, sticky=tk.S+tk.E)
		
		self.resize(self.side_frame, 2, 0)
		self.side_frame.grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
		
		close_button = tk.Button(self.side_frame, text="Close Chat", command=self.tab.destroy)
		close_button.grid(padx=5, pady=5)
		settings_button = tk.Button(self.side_frame, text="Settings", command=None)
		settings_button.grid(padx=5, pady=5)
		userlist_button = tk.Button(self.side_frame, text="User List", command=None)
		userlist_button.grid(padx=5, pady=5)

	def resize(self, widget, rowcol, num):
		if rowcol == 1:
			widget.rowconfigure(num, weight=1)
		elif rowcol == 2:
			widget.columnconfigure(num, weight=1)
		else:
			widget.rowconfigure(num, weight=1)
			widget.columnconfigure(num, weight=1)

		
	def display_messages(self):
		cookies = { "session": "GLIH5XTNKKMRAN" }
		chat = "theoubliette"
		counter = -1
		r = requests.post("http://charatrp.com/chat_ajax/messages", cookies=cookies, data={ "chat": chat, "after": counter })
		first_query = json.loads(r.text)

	#	for message_data in first_query['messages']:
	#		msg = message_data['line'].encode("utf8")
	#		self.message_area.config(state=tk.NORMAL)
	#		self.message_area.insert(tk.END, msg)

		counter = len(first_query['messages'])
		
		while True:
			try:
				chatLine = json.loads(requests.post("http://charatrp.com/chat_ajax/messages", cookies=cookies, data={ "chat": chat, "after": counter }).text)
				tid = chatLine['messages'][0]['counter']
				message = chatLine['messages'][0]['line']
				
				self.message_area.config(state=tk.NORMAL)
				self.message_area.insert(tk.END, message)
				
				counter = chatLine['messages'][0]['id'] + 1
			except:
				print "oops"

def main():

	root = tk.Tk()
	root.geometry("800x600+50+50")
	app = MainWin(root)
	root.mainloop()  


if __name__ == '__main__':
	main()  

	
	
	
'''
	def send_message(self, msg):
		#This just prints the message to the sample text area for testing. 
		#Later this function should just send the message to the server.
		#self.message_area.config(state=tk.NORMAL)
		#self.message_area.insert(tk.END, "\nPerson2: " + self.message_var.get())
		#self.message_entry.delete(0, tk.END)
		#requests.post("http://charatrp.com/chat_ajax/post", cookies=cookies, data={ "chat": chat, "line":  msg })

'''
