import platform
import os
from celery import Celery
from src.autoRsync import autoRsync

id = platform.uname()


source = input("Enter Source Directory: ")
dest = input("Enter Destination Directory: ")


if platform.system() == 'Windows':
    autoRsync.windows(source, dest)
elif platform.system() =='Darwin':
    if id[5] == 'x86_64':
        autoRsync.macos_x86(source, dest)
    else:
        autoRsync.macos_arm(source, dest)
elif platform.system() == 'linux':
    if id[5] == 'x86_64':
        autoRsync.linux_x86(source, dest)
    else:
        autoRsync.linux_arm(source, dest)
elif platform.system() == 'freebsd':
    autoRsync.freebsd(source, dest)

else:
    print("Unsupported Operating system", id[0])