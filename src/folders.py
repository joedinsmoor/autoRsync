import os
import threading
from src.autoRsync import autoRsync


class foldersync:

    def cascading(self, dest, tempsource):
        if not os.path.isdir(dest + "/" + tempsource): # type: ignore
            try:
                os.makedirs(dest + "/" + tempsource) # type: ignore
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