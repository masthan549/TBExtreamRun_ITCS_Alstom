import os, sys, time, re
from os import path
import subprocess
from subprocess import *
from tkinter import messagebox


def script_exe(LDRAToolsuitePath, sourceFilePath, tcfPath, TkObject_ref, statusBarText):

    
    #Set the curret directory
    os.chdir('.')    
    tcfPath = tcfPath.replace('/', '\\')    
    tcfName = tcfPath.split("\\")[len(tcfPath.split("\\"))-1]
    tcfPath = tcfPath.split("\\")[:len(tcfPath.split("\\"))-1]
    tcfPath = "\\".join(tcfPath) 
    
    print(tcfPath)
    print(tcfName)    
    
    statusBarText.set("TBExtream Batch file execution in progress, please wait...")
    
    ################# 1. Execute the batch file ####################### 
    batchFile = os.getcwd()+"\\Executetcf.bat"
    #Check if batch file present in given location
    if not path.exists(batchFile):           
        messagebox.showerror('Error','Please make sure vital and non_vital batch files are present in application folder!')
        TkObject_ref.destroy()
        sys.exit()            
    

    p = subprocess.Popen([batchFile, tcfName, tcfPath, sourceFilePath], stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate()
    
    #This makes the wait possible
    p_status = p.wait()

    print("\n Number of Errors seen during batch file execution: "+str(stderr))

    if(len(str(stderr))) > 0:
        messagebox.showerror('Error','During batch file execution encountered error!.') 
        TkObject_ref.destroy()
        sys.exit()        


    statusBarText.set("DONE!!")    
    messagebox.showinfo('DONE!!',"TB Extream execution done!")
    TkObject_ref.destroy()
    sys.exit()
