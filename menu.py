
import os
from celery import Celery
from src.autoRsync import autoRsync
import threading
import sys


args = sys.argv
n = len(sys.argv)
source = ''
dest = ''

print("         - - - - Welcome to autoRsync v1.0 - - - -")
print("        I wrote this for my own use, primarily for")
print("automated backups of my personal machines and devices to a local")
print("server, and automated backups from there to S3 and Google Drive")


print("\n\nautoRsync is free to use, modify, and distribute as you see fit, as long as")
print("the GNU GPL 3 license is abided by. It can be viewed by opening the LICENSE file in the master directory\n\n")


if not (args.__contains__('-h')):
    print("If you need help, please run autoRsync with the -h flag, like this: 'python3 menu.py -h'")
else:
    print("        - - - - Help Menu - - - -       \n")

if(args.__contains__("-s")):
    i = args.index("-s")
    source = args[i + 1]

if(args.__contains__("-d")):
    j = args.index("-d")
    dest = args[j + 1]


if(args.__contains__("-h")):
    help = "-s  : specifies source directory/file\n-d  : specifies destination directory\n-h  : prints this help dialog\n"
    print(help)
    exit()

if source == '':
    source = input("Enter Source Directory: ")
if dest == '':
    dest = input("Enter Destination Directory: ")

mtf = 0



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
            if not os.path.isdir(dest + "/" + tempsource):
                try:
                    os.makedirs(dest + "/" + tempsource)
                except OSError:
                    print(f"Directory {dest + tempsource} exists")
            tempfiles = os.listdir(tempsource)
            for tempfile in tempfiles:
                temptemp = tempsource + "/" + tempfile
                try:
                    tt = threading.Thread(target=autoRsync.find_os(temptemp, dest))
                except:
                    pass
        print(tempsource)
        t = threading.Thread(target=autoRsync.find_os(tempsource, dest))
    if(os.listdir(source) != os.listdir(dest)):
        print("Some files skipped:\n")
        for file in files:
            if file not in dest:
                print(file)
            

else:

    autoRsync.find_os(source, dest)