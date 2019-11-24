import os
import shutil
import json
from datetime import datetime

src = r"C:\Users\jagan\Desktop\BackupSchedler\SRC"
dst = r"C:\Users\jagan\Desktop\BackupSchedler\DES"


def BackUp(src, dst, file):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, False, None)
            print("Copying from " + s + " to " + d)
            file.write("Copying from " + s + " to " + d + "\n")
        else:
            shutil.copy2(s, d)
            print("Copying from " + s + " to " + d)
            file.write("Copying from " + s + " to " + d + "\n")
    return True

def ensure_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        

def main():
    global dst
    print("BackupFiles from " + src + " to " + dst)
    now = datetime.now()
    #print("now =", now)
    dt_string = now.strftime("\BackUp_%d_%m_%Y_%H_%M_%S")
    #print("date and time =", dt_string)
    dst += dt_string
    ensure_dir(dst)
    completeName = os.path.join(dst, "Log" +".txt") 
    logFile = open(completeName,"w+")
    logFile.write("date and time = " + dt_string)
    logFile.write("\n===========================\n")
    #dst = dst + dt_string
    BackUp(src, dst, logFile)
    logFile.close() 
    

if __name__== "__main__":
    main()