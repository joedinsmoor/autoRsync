
import os
from celery import Celery
from src.autoRsync import autoRsync
import threading




source = input("Enter Source Directory: ")
dest = input("Enter Destination Directory: ")


if not (os.path.isdir(dest)):
    print(f"Destination directory {dest} does not exist, create now? (y/n)")
    opt = input()
    if(opt == 'y' or 'yes'):
        os.makedirs(dest)
if source.endswith("/"):
    files = os.listdir(source)
    mtf = 1 #flag for multithreading use


if(mtf):
    for file in files: #create a thread for each file in directory, call correct autoRsync member function and run in parallel
        tempsource = source + file
        if(os.path.isdir(tempsource)): # RECURSIVE BULLSHIT IS GREAT and DOESN'T WORK
            tempfiles = os.listdir(tempsource)
            for tempfile in tempfiles:
                temptemp = tempsource + tempfile
                tt = threading.Thread(target=autoRsync.find_os(temptemp, dest))
        print(tempsource)
        t = threading.Thread(target=autoRsync.find_os(tempsource, dest))

else:

    autoRsync.find_os(source, dest)