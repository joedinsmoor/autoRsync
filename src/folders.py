import os
import threading
from autoRsync import autoRsync


class foldersync:

    def cascading(dest, tempsource):
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

    #Take in directory, find directories, drill down and copy folder structure
    #Copy files to correct locations using hashmap
    #????
    #Profit