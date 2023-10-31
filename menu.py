import platform
from src.autoRsync import *

id = platform.uname()

if id[0] == 'nt':
    windows()
elif id[0] =='Darwin':
    if id[5] == 'x86_64':
        macos_intel()
    else:
        macos_x86()
elif id[0] == 'linux':
    if id[5] == 'x86_64':
        linux_x86()
    else:
        linux_arm()
elif id[0] == 'freebsd':
    freebsd()

else:
    print("Unsupported Operating system", id[0])