import platform
import os
import celery
from src.autoRsync import *

id = platform.uname()


source = input("Enter Source Directory: ")
dest = input("Enter Destination Directory: ")

if platform.system() == 'Windows':
    windows(source, dest)
elif platform.system() =='Darwin':
    if id[5] == 'x86_64':
        macos_x86(source, dest)
    else:
        macos_arm
elif platform.system() == 'linux':
    if id[5] == 'x86_64':
        linux_x86(source, dest)
    else:
        linux_arm(source, dest)
elif platform.system() == 'freebsd':
    freebsd(source, dest)

else:
    print("Unsupported Operating system", id[0])