from tkinter import *
from tkinter import ttk


class MainWindow:
    

    def __init__(self, addSiteBlockButtonCommand):
        self.window = Tk()
        self.window.title("Site Blocker")
        self.window.geometry("850x500")

        self.addBlockSite(addSiteBlockButtonCommand)
        self.listOfBlocedkSite()
    
        self.window.mainloop()
        


    def addBlockSite(self, addButtonCommand):

        siteUrl = StringVar()

        frame = ttk.Frame(self.window, padding='20', borderwidth='2', relief='ridge')
        frame.pack(side=TOP, fill=X)

        ttk.Label(frame, text="Site Url : ").grid(column=0, row=0)
        siteNameEntry = ttk.Entry(frame, textvariable=siteUrl).grid(column=1, row=0,)
        addButton = ttk.Button(frame, text="Add", command=addButtonCommand).grid(column=2, row=0, padx=10)



    def listOfBlocedkSite(self):
   
        frame = ttk.Frame(self.window, padding='20', borderwidth=2, relief='ridge')
        frame.pack( fill=BOTH, expand=1)
        ttk.Label(frame, text="List of blocked sites : ").grid(column=0, row=0)
