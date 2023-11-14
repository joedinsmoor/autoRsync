import sysrsync
import os
import platform


class autoRsync:


    '''
    find_os will take in the source and destination directories or files, determine what OS both 
    directories are hosted on, and make the handshake with the correct method for the correct OS
    '''

    def find_os(source, dest):
        id = platform.uname()

        if platform.system() == 'Windows':
            autoRsync.windows(source, dest)
        elif platform.system() =='Darwin':
            if id[5] == 'i386':
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
        '''
    when windows is detected, autoRsync will call sysrsync and copy
    a selected folder to a selected destination
    '''
    def windows(source, dest):
        sysrsync.run(source=source, destination=dest)
        fname = source.split("/")
        nName = dest + fname[len(fname)-1]
        if os.path.isfile(dest + fname[len(fname)-1]):
            print(f"Function succeeded, file located at: ", nName)
    '''
    when apple silicon based macos is detected, autoRsync will call sysrsync and copy
    a selected folder to a selected destination
    '''
    def macos_arm(source, dest):
        #print("Starting for macos_arm\n\n")
        sysrsync.run(source=source, destination=dest)
        fname = source.split("/")
        nName = dest + fname[len(fname)-1]
        if os.path.isfile(dest + fname[len(fname)-1]):
            print(f"Function succeeded, file located at: ", nName)


    '''
    when linux is detected, autoRsync will call sysrsync and copy
    a selected folder to a selected destination
    '''
    def linux_x86(source, dest):
        sysrsync.run(source=source, destination=dest)
        fname = source.split("/")
        nName = dest + fname[len(fname)-1]
        if os.path.isfile(dest + fname[len(fname)-1]):
            print(f"Function succeeded, file located at: ", nName)

    def linux_arm(source, dest):
        sysrsync.run(source=source, destination=dest)
        fname = source.split("/")
        nName = dest + fname[len(fname)-1]
        if os.path.isfile(dest + fname[len(fname)-1]):
            print(f"Function succeeded, file located at: ", nName)


    '''
    when intel based macos is detected, autoRsync will call sysrsync and copy
    a selected folder to a selected destination
    '''
    def macos_x86(source, dest):
        sysrsync.run(source=source, destination=dest)
        fname = source.split("/")
        nName = dest + fname[len(fname)-1]
        if os.path.isfile(dest + fname[len(fname)-1]):
            print(f"Function succeeded, file located at: ", nName)

    def freebsd(source, dest):
        sysrsync.run(source=source, destination=dest)
        fname = source.split("/")
        nName = dest + fname[len(fname)-1]
        if os.path.isfile(dest + fname[len(fname)-1]):
            print(f"Function succeeded, file located at: ", nName)