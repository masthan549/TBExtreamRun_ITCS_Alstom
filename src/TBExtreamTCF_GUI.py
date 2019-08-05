from tkinter import Label, Button, Entry, Radiobutton 
import tkinter as tk
from tkinter import messagebox, filedialog, StringVar, SUNKEN, W, X, BOTTOM
from os import path
import threading, sys
import os
from tkinter.filedialog import askopenfilename
import TBExtreamSetup

class GUI_COntroller:
    '''
	   This class initialize the required controls for TkInter GUI
	'''
    def __init__(self,TkObject):

        #Load company image
        Imageloc=tk.PhotoImage(file='../Images/alstom_logo.gif')		
        label3=Label(image=Imageloc,)
        label3.image = Imageloc		
        label3.place(x=200,y=20)

        global TkObject_ref, entryText_LDRAToolPath, entryText_SourceCodeFilePath, entryText_TCFFile, AnalyseDirRunBatchButton

        #1. select LDRA Tool suite directory
        TkObject_ref = TkObject
        LDRAToolsuitePath=Button(TkObject_ref,activebackground='green',borderwidth=3, anchor="w", text='1. Select LDRA Tool suite path:',width=30, command=lambda:GUI_COntroller.selectResDirectory("LDRAPath"), cursor="hand2")
        LDRAToolsuitePath.place(x=30,y=120)
        LDRAToolsuitePath.config(font=('helvetica',10,'bold'))	

        #1. This is text box where LDRA tool suite directory will be shown to user
        entryText_LDRAToolPath = tk.StringVar()		
        Entry_LDRAToolSuitePath= Entry(TkObject_ref, width=78, textvariable=entryText_LDRAToolPath, bd=1)
        Entry_LDRAToolSuitePath.place(x=290,y=124)					
        Entry_LDRAToolSuitePath.config(font=('helvetica',10), state="readonly")	


 
        #2. select TCF file directory
        TCFFile=Button(TkObject_ref,activebackground='green',borderwidth=3, anchor="w", text='2. Select TCF file:',width=30, command=lambda:GUI_COntroller.selectResDirectory("TCFFile"), cursor="hand2")
        TCFFile.place(x=30,y=200)
        TCFFile.config(font=('helvetica',10,'bold'))	

        #2. This is text box where TCF name will be shown to the user
        entryText_TCFFile = tk.StringVar()		
        Entry_TCF= Entry(TkObject_ref, width=78, textvariable=entryText_TCFFile, bd=1)
        Entry_TCF.place(x=290,y=200)			
        Entry_TCF.config(font=('helvetica',10), state="readonly")	

        #3. select sysearch file
        SourceCodeFilePath=Button(TkObject_ref,activebackground='green',borderwidth=3, anchor="w", text='3. Select c file:',width=30, command=lambda:GUI_COntroller.selectResDirectory("SourceCode"), cursor="hand2")
        SourceCodeFilePath.place(x=30,y=280)
        SourceCodeFilePath.config(font=('helvetica',10,'bold'))    

        #3. This is text box where source file directory will be shown to user
        entryText_SourceCodeFilePath = tk.StringVar()        
        Entry_sysearchFilePath= Entry(TkObject_ref, width=78, textvariable=entryText_SourceCodeFilePath, bd=1)
        Entry_sysearchFilePath.place(x=290,y=280)            
        Entry_sysearchFilePath.config(font=('helvetica',10), state="readonly") 


        #Exit Window		
        closeButton=Button(TkObject_ref,activebackground='green',borderwidth=4, text='Close Window', command=GUI_COntroller.exitWindow)
        closeButton.place(x=570,y=360)	
        closeButton.config(font=('helvetica',11,'bold'))	


        #select sequence files directory
        AnalyseDirRunBatchButton=Button(TkObject_ref,activebackground='green',borderwidth=4, text='Run TBExtream',width=25, command=GUI_COntroller.RunTest)
        AnalyseDirRunBatchButton.place(x=200,y=360)
        AnalyseDirRunBatchButton.config(font=('helvetica',11,'bold'))		           
            
        #read the data from saved preference if it is saved already
        GUI_COntroller.readDataFromSavedPref()  

    def writeDataIntoSavedPref():

        dictSavedPref = {}
        fPtr = open("../Images/savedPref.txt","w")
        dictSavedPref["LDRAToolsuite"] = entryText_LDRAToolPath.get()
        dictSavedPref["TCFFile"] = entryText_TCFFile.get()
        dictSavedPref["SourceCode"] = entryText_SourceCodeFilePath.get()                                        
        fPtr.write(str(dictSavedPref))
        fPtr.close()

    def readDataFromSavedPref():
        if os.path.exists('../Images/savedPref.txt'):
            fPtr = open("../Images/savedPref.txt")
            for lineText in fPtr:
                dictInfoOfSavedPrefDir = eval(lineText)
                if 'LDRAToolsuite' in dictInfoOfSavedPrefDir.keys():                      
                    entryText_LDRAToolPath.set(dictInfoOfSavedPrefDir['LDRAToolsuite']) 
                if 'TCFFile' in dictInfoOfSavedPrefDir.keys():                      
                    entryText_TCFFile.set(dictInfoOfSavedPrefDir['TCFFile']) 
                if 'SourceCode' in dictInfoOfSavedPrefDir.keys():                      
                    entryText_SourceCodeFilePath.set(dictInfoOfSavedPrefDir['SourceCode'])                                                                                                                               

    def selectResDirectory(dirSelectionType): 
        global entryText_LDRAToolPath, entryText_SourceCodeFilePath, entryText_TCFFile
        currdir = os.getcwd()

        if dirSelectionType == "LDRAPath":
            selectedDir_res = filedialog.askdirectory(initialdir=currdir, title='Please select a LDRA tool suite directory')
            
            if len(selectedDir_res)> 0:
                if not path.isdir(selectedDir_res):
                    entryText_LDRAToolPath.set("")			
                    messagebox.showerror('Error','Please select a valid directory!')
                else:
                    entryText_LDRAToolPath.set(str(selectedDir_res))
        elif dirSelectionType == "TCFFile":
                selectedFile_res = askopenfilename(initialdir=currdir, title='Please select TCF file', filetypes=(("sysearch files", "*.tcf"), ("all files", "*.*")))
                
                if len(selectedFile_res)> 0:
                    if not path.exists(selectedFile_res):
                        entryText_TCFFile.set("")			
                        messagebox.showerror('Error','Please select a valid TCF file!')
                    else:
                        entryText_TCFFile.set(str(selectedFile_res))						
        elif dirSelectionType == "SourceCode":
                selectedFile_res = askopenfilename(initialdir=currdir, title='Please select a Source code file', filetypes=(("sysearch files", "*.c"), ("all files", "*.*")))
                
                if len(selectedFile_res)> 0:
                    if not path.exists(selectedFile_res):
                        entryText_SourceCodeFilePath.set("")			
                        messagebox.showerror('Error','Please select a valid source code file!')
                    else:
                        entryText_SourceCodeFilePath.set(str(selectedFile_res))	

    def exitWindow():
            TkObject_ref.destroy()

    def RunTest():

        if len(entryText_LDRAToolPath.get()) > 0:
            if len(entryText_SourceCodeFilePath.get()) > 0:
                if (len(entryText_TCFFile.get()) > 0): 
                    ProjectDirAnalysis.RunAnalysis()
                else:
                    messagebox.showerror('Error','Please select valid TCF file!')                                  
            else:
                messagebox.showerror('Error','Please select Source code file!')
        else:
            messagebox.showerror('Error','Please select LDRA tool path!')    

class ProjectDirAnalysis:
    def RunAnalysis(): 

        global statusBarText
        AnalyseDirRunBatchButton.config(state="disabled")

        statusBarText = StringVar()
        StatusLabel = Label(TkObject_ref, textvariable=statusBarText, fg="green", bd=1,relief=SUNKEN,anchor=W) 
        StatusLabel.config(font=('helvetica',11,'bold'))
        StatusLabel.pack(side=BOTTOM, fill=X)

        GUI_COntroller.writeDataIntoSavedPref();
        thread = threading.Thread(target=TBExtreamSetup.script_exe, args = (entryText_LDRAToolPath.get(), entryText_SourceCodeFilePath.get(), entryText_TCFFile.get(), TkObject_ref, statusBarText))                                
        thread.start()

if __name__ == '__main__':	

    root = tk.Tk()
       
    #Change the background window color
    root.configure(background='#b7bbc7')     
       
    #Set window parameters
    root.geometry('850x680')
    root.title('TB Extream batch run')
       
    #Removes the maximizing option
    root.resizable(0,0)
       
    ObjController = GUI_COntroller(root)
       
    #keep the main window is running
    root.mainloop()
    sys.exit()
