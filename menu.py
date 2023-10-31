import platform
from src.autoRsync import *

id = platform.uname()

if platform.system() == 'Windows':
    windows()
elif platform.system() =='Darwin':
    if id[5] == 'x86_64':
        macos_intel()
    else:
        macos_x86()
elif platform.system() == 'linux':
    if id[5] == 'x86_64':
        linux_x86()
    else:
        linux_arm()
elif platform.system() == 'freebsd':
    freebsd()

else:
    print("Unsupported Operating system", id[0])