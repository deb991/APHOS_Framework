from tkinter import *
import tkinter.messagebox
import tkinter.font
import os
import sys
import subprocess


desktopTaskBar = Tk()

w = 1595 # width for the Tk desktopTaskBar
h = 40 # height for the Tk desktopTaskBar

# get screen width and height
ws = desktopTaskBar.winfo_screenwidth() # width of the screen
hs = desktopTaskBar.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk desktopTaskBar window
x = (ws/1) - (w/1)
y = (hs/1) - (h/1)

desktopTaskBar.geometry('%dx%d+%d+%d' % (w, h, x, y))

desktopTaskBar.geometry("1595x40")
desktopTaskBar.resizable(0,0)
desktopTaskBar.configure(background='grey')
desktopTaskBar.wm_attributes("-transparentcolor", "grey")
desktopTaskBar.overrideredirect(1)
desktopTaskBar.lift()


#helv9 = tkFont.Font(family='Helvetica', size=9, weight=tkFont.BOLD)
helv9 = tkinter.font.Font(family='Helvetica', size=7, weight='bold')
tkinter.font.families()
ButtFontColor = '#00A7FB'


def __init__(self):
    Tk.Tk.__init__ ( self )
    self.title ( "Handling WM_DELETE_WINDOW protocol" )
    self.geometry ( "500x300+500+200" )
    self.make_topmost ()
    self.protocol ( "WM_DELETE_WINDOW", self.on_exit )

def on_Exit(self):
    """When you click to exit, this function is called"""
    if tkinter.messagebox.askyesno ( "Exit", "Do you want to quit the application?" ):
        self.destroy ()

def center(self):
    """Centers this Tk window"""
    self.eval ( 'tk::PlaceWindow %s center' % desktopTaskBar.winfo_pathname ( desktopTaskBar.winfo_id () ) )

def make_topmost(self):
    """Makes this window the topmost window"""
    self.lift ()
    self.attributes ( "-topmost", 1 )
    self.attributes ( "-topmost", 0 )

def Search():
    print('Search')
b = Button ( desktopTaskBar, text="Search", font = helv9, command=Search, padx=8, bg='black', fg=ButtFontColor)
b.place(anchor=SW)
b.pack (side = LEFT)

def OUTLOOK():
    print('OUTLOOK')
    os.chdir ( 'C:\\Program Files\\Microsoft Office\\root\\Office16\\' )
    os.startfile (r"C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE")
b = Button ( desktopTaskBar, text="OutLook", font = helv9, command=OUTLOOK, padx=6, bg="black", fg=ButtFontColor)
b.place(anchor=SW)
b.pack (side = LEFT)

def MSSequalServer():
    print('Initiating SEQUAL MANAGEMENT STUDIO')
    os.chdir("C:\\Program Files\\Microsoft SQL Server\\100\\Tools\\Binn\\VSShell\\Common7\\IDE")
    os.startfile ( r"C:\Program Files\Microsoft SQL Server\100\Tools\Binn\VSShell\Common7\IDE\\Ssms.exe")
b = Button ( desktopTaskBar, text="Sequal Server", font = helv9, command=MSSequalServer, padx=6, bg="black", fg=ButtFontColor)
b.place(anchor=SW)
b.pack (side =LEFT)

def PLSql():
    print('Initiating SQL developer')
    os.chdir("C:\\Users\\Debashis.Biswas\\Software\\sqldeveloper")
    os.startfile ( r"C:\\Users\\Debashis.Biswas\\Software\\sqldeveloper\\sqldeveloper.exe")
b = Button ( desktopTaskBar, text="PL/ SQL",font = helv9, command=PLSql, padx=6, bg="black", fg=ButtFontColor)
b.place(anchor=SW)
b.pack (side = LEFT)

def BMCControlM():
    print('service start DDF')
b = Button ( desktopTaskBar, text="Control M",font = helv9, command=BMCControlM, padx=6, bg="black", fg=ButtFontColor)
b.place(anchor=SW)
b.pack (side = LEFT)

def PyCharmIDE():
    print('service start DDF')
b = Button ( desktopTaskBar, text="PyCharm",font = helv9, command=PyCharmIDE, padx=6, bg="black", fg=ButtFontColor)
b.place(anchor=SW)
b.pack (side = LEFT)

def Visual_BasicIDE():
    print('service start DDF')
b = Button ( desktopTaskBar, text="Visual Basic",font = helv9, command=Visual_BasicIDE, padx=6, bg="black", fg=ButtFontColor)
b.place(anchor=SW)
b.pack (side = LEFT)

def Exit():
    print('EXIT')
    desktopTaskBar.destroy()
b = Button ( desktopTaskBar, text="Exit",font = helv9, command=Exit, padx=3, bg="black", fg='red')
b.place(anchor=SW)
b.pack (side = RIGHT)


def File_Manager():
    print('File manager')
b = Button ( desktopTaskBar, text="File Manager", font=helv9, command=File_Manager, padx=6, bg="black", fg=ButtFontColor )
b.place ( anchor=SW )
b.pack ( side= LEFT )

def QUERY_LIBRARY():
    print('Query Library')
    os.startfile ( r"C:\Program Files\Microsoft SQL Server\100\Tools\Binn\VSShell\Common7\IDE\\Ssms.exe" )
b = Button ( desktopTaskBar, text="QUEERY LIBRARY", font=helv9, command=QUERY_LIBRARY, padx=6, bg="black", fg=ButtFontColor )
b.place ( anchor=SW )
b.pack ( side= LEFT )

mainloop ()
