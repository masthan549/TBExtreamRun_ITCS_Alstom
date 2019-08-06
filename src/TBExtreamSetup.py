import os, sys, time, re
from os import path
import subprocess
from subprocess import *
from tkinter import messagebox


def script_exe(LDRAToolsuitePath, sourceFilePath, tcfPath, TkObject_ref, statusBarText):

    
    #Set the curret directory
    os.chdir('.')    
    sourceFilePath = sourceFilePath.replace("/","\\")   
    tcfPath = tcfPath.replace('/', '\\')    
    tcfName = tcfPath.split("\\")[len(tcfPath.split("\\"))-1]
    tcfPath = tcfPath.split("\\")[:len(tcfPath.split("\\"))-1]
    tcfPath = "\\".join(tcfPath) 
  
    
    statusBarText.set("TBExtream Batch file execution in progress, please wait...")
    
    ################# 1. Execute the batch file ####################### 
    batchFile = os.getcwd()+"\\Executetcf.bat"
    #Check if batch file present in given location
    if not path.exists(batchFile):           
        messagebox.showerror('Error','Please make sure vital and non_vital batch files are present in application folder!')
        TkObject_ref.destroy()
        sys.exit()

    try:
        tcfPath = tcfPath.replace("\\","/")
        p = subprocess.Popen([batchFile, tcfName, tcfPath, sourceFilePath, LDRAToolsuitePath], stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        stdout, stderr = p.communicate()
    
        #This makes the wait possible
        p_status = p.wait()

        print("\n Number of Errors seen during batch file execution: "+str(stderr))

    except Exception as e:
        messagebox.showerror("Error","During batch file execution exception raised!"+str(e))
        TkObject_ref.destroy()
        sys.exit()           

    statusBarText.set("DONE!!")    
    messagebox.showinfo('DONE!!',"TB Extream execution done!")
    TkObject_ref.destroy()
    sys.exit()
