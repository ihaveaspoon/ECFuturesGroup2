#                    #
# Real World Project #
#      Group 2       #
#                    #

#importing libraries/packages
from tkinter import*

#Creating the root screen
root = Tk()
root.title("EC Futures - CRM System")
root.geometry("733x150")
root.configure(background="white")

#Creating the frame for the widgets
app = Frame(root)
app.grid()
app.configure(background="white")

#Title for the main page
Main_title = Label(app)
Main_title.pack()
Main_title.configure(text="EC Futures - CRM System",font=("Verdana",30),background="white")

#Functions for Navigation Bar
def AddPage():
    new = Tk()
    new.title("Add Page")
    new.geometry("1000x300")
    Add = Frame(new)

def EditPage():
    new = Tk()
    new.title("Edit Page")
    new.geometry("1000x300")
    Edit = Frame(new)

def ExportPage():
    new = Tk()
    new.title("Export Page")
    new.geometry("1000x300")
    Export = Frame(new)

def AppointmentPage():
    new = Tk()
    new.title("Appointment Page")
    new.geometry("1000x300")
    Appointment = Frame(new)

def HelpPage():
    new = Tk()
    new.title("Help Page")
    new.geometry("1000x300")
    Help = Frame(new)
#Navigation Bar#
#------------------------------------
addbtn = Button(app,command=AddPage)
addbtn.pack(ipadx=15, pady=15, side=LEFT)
addbtn.configure(text="Add",font=("Verdana",15),background="white")
#------------------------------------
editbtn = Button(app,command=EditPage)
editbtn.pack(ipadx=20, pady=15, side=LEFT)
editbtn.configure(text="Edit",font=("Verdana",15),background="white")
#------------------------------------
exportbtn = Button(app,command=ExportPage)
exportbtn.pack(ipadx=25, pady=15, side=LEFT)
exportbtn.configure(text="Export",font=("Verdana",15),background="white")
#------------------------------------
appointmentsbtn = Button(app,command=AppointmentPage)
appointmentsbtn.pack(ipadx=30, pady=15, side=LEFT)
appointmentsbtn.configure(text="Appointments",font=("Verdana",15),background="white")
#------------------------------------
helpbtn = Button(app,command=HelpPage)
helpbtn.pack(ipadx=35, pady=15, side=LEFT)
helpbtn.configure(text="Help Page",font=("Verdana",15),background="white")

#Loop to show the main window 
root.mainloop()
