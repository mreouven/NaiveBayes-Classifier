# -*- coding: cp1252 -*-
import Tkinter as tk
import ttk
import Tkconstants, tkFileDialog
import os
import pickle
import tkFileDialog
from FileDialog import LoadFileDialog

class FilenameEntry(tk.Frame):
    """a widget for displaying a input edit box and a browser to choose a file """
    def __init__(self, master, text):
        tk.Frame.__init__(self, master,background='white')
        tk.Label(self, text=text,width=15,background='white').pack(side="left")
        self.filename = tk.StringVar()
        tk.Entry(self, textvariable=self.filename, width=40,background='white').pack(side="left", fill="x",padx=15)
        tk.Button(self, text="Browse...",background='black',foreground='white', command=self.choiceDirectory).pack(side="right")

    def browse(self):
        file = LoadFileDialog(self).go(pattern='*')
        if file:
            self.filename.set(file)
            
    def choiceDirectory(self):
        self.dir = tkFileDialog.askdirectory()
        if len(self.dir) > 0:
            self.filename.set(self.dir)
    
    def get(self):
        return self.filename.get()

    def put(self,val):
        self.filename.set(val)

class BinSelect(tk.Frame):
    """a widget for displaying a input edit box and a browser to choose a file """
    def __init__(self, master, text):
        tk.Frame.__init__(self, master,background='white')
        tk.Label(self, text=text,width=15,background='white').pack(side="left")
        self.select = tk.StringVar()
        tk.Entry(self, textvariable=self.select, width=40,background='white').pack(side="left", fill="x",padx=15)
    def get(self):
        return self.select.get()
    def put(self,val):
        self.select.set(val)



class Example(tk.Frame):
    def __init__(self, parent):
        self.create_widgets(parent)
    def create_widgets(self, parent):
        #frame editation
        tk.Frame.__init__(self, parent, bg='white',relief="raised", bd=2,width=100,height=200)
        #object creation
        self.filename = FilenameEntry(self, "Source filename: ")
        self.binSelection=BinSelect(self, "enter nb of bin: ")
        self.buildButton = tk.Button(self,borderwidth=2, text="Build",width=10, command=self.build)
        self.clasify = tk.Button(self,borderwidth=2, text="Classify",width=10, command=self.choiceDirectory)
        tk.Label(self, text='Naive Bayes Classifier', font=('Helvetica', 12, 'italic bold'),background='black', foreground='white').pack(side="top", expand="no", fill="x")
        #objet implemantage
        tk.Label(self, text="\nEnter a filename and " + "select an action",background='white').pack(side="top")
        self.filename.pack(side="top", fill="x")
        self.binSelection.pack(side="top", fill="x")
        self.buildButton.pack( padx=3,pady=3)
        self.clasify.pack( padx=3,pady=3)
    def build(self):
        print(self.filename.get()+"\n"+self.binSelection.get())
    def choiceDirectory(self):
        self.rep = tkFileDialog.askdirectory()
        if len(rep) > 0:
            self.resultLabel.configure(text=str(rep))



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Naive Bayes Classifier")
    Example(root).pack(fill="both", expand=True)
    root.mainloop()

