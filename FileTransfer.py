
import tkinter
from tkinter import *
from tkinter import filedialog

import shutil
import os
import datetime 



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height= False)
        self.master.geometry('{}x{}'.format(450,200))
        self.master.title('Check files')
        self.master.config(bg='whitesmoke')

        self.fileFrom = StringVar()
        self.fileTo = StringVar()
        
        self.instruction = Label(self.master, text='Select folders from Directory and initiate updates')
        self.instruction.grid(row=0, column=0, columnspan=3)
                                 
        self.btnBrowse1 = Button(self.master, text='AskDirectoryFrom', width=15, height=1, command=self.askDirFrom)
        self.btnBrowse1.grid(row=1, column=0, padx=(20,0),pady=(5,0), sticky=W)
        
        self.btnBrowse2 = Button(self.master, text='AskDirectoryTo', width=15, height=1, command=self.askDirTo)
        self.btnBrowse2.grid(row=2, column=0, padx=(20,0), pady=(10,10), sticky=W)

        self.btnCheck = Button(self.master, text='Check&Transfer', width=15, height=2, command=self.UpdateFiles)
        self.btnCheck.grid(row=3, column=0, padx=(20,0), pady=(0,10), sticky=W)

        self.btnClose = Button(self.master, text='Close Program', width=15, height=2, command=self.close)
        self.btnClose.grid(row=3, column=2, padx=(150,20))
        
        self.entryBox1 = Entry(self.master, textvariable=self.fileFrom, font=("Roboto",16), fg='black', bg='white')
        self.entryBox1.grid(row=1, column=1, columnspan=2, padx=(20,0), pady=(5,0))

        self.entryBox2 = Entry(self.master, textvariable=self.fileTo, font=("Roboto",16), fg='black', bg='white')
        self.entryBox2.grid(row=2, column=1, columnspan=2, padx=(20,0))
        
    def askDirFrom(self):
        folderSelected = filedialog.askdirectory()  # user selected "from" folder and set file path as StringVar()
        self.fileFrom.set(folderSelected)

    def askDirTo(self):
        folderSelected = filedialog.askdirectory()  # user selected "to" folder and set file path as StringVar()
        self.fileTo.set(folderSelected)
    
    def close(self):
        self.master.destroy()

    def UpdateFiles(self):

        #get where the source of the files are
        source = self.entryBox1.get()
        #get the destination path to 
        dest = self.entryBox2.get()
        #get files mod time and define a timeframe of within the last 24 hours
        for files in os.listdir(source):
            srcFile = os.path.join(source, files)
            pathTime = os.path.getmtime(srcFile)
            before = datetime.datetime.now() - datetime.timedelta(hours=24)
            modTime =datetime.datetime.fromtimestamp(pathTime)
        # checking for new files or changed files within th last 24 hours to move to
        #or overwrite/ update existing file in the destination folder  
            if modTime > before: 
                destFolder = os.path.join(dest, files)
                shutil.move(srcFile, destFolder)






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
