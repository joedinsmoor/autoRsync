import sysrsync
import os


class autoRsync:
    '''
    when windows is detected, autoRsync will call sysrsync and copy
    a selected folder to a selected destination
    '''
    def windows(source, dest):
        sysrsync.run(source=source, destination=dest)
        if os.path.file(dest):
            print(f"Function succeeded, file located at: ", dest)
    '''
    when apple silicon based macos is detected, autoRsync will call sysrsync and copy
    a selected folder to a selected destination
    '''
    def macos_arm(source, dest):
        print("Starting for macos_x86\n\n")
        sysrsync.run(source=source, destination=dest)
        if os.path.isfile(dest):
            print(f"Function succeeded, file located at: ", dest)


    '''
    when linux is detected, autoRsync will call sysrsync and copy
    a selected folder to a selected destination
    '''
    def linux_x86(source, dest):
        sysrsync.run(source=source, destination=dest)
        if os.path.isfile(dest):
            print(f"Function succeeded, file located at: ", dest)

    def linux_arm(source, dest):
        sysrsync.run(source=source, destination=dest)
        if os.path.isfile(dest):
            print(f"Function succeeded, file located at: ", dest)


    '''
    when intel based macos is detected, autoRsync will call sysrsync and copy
    a selected folder to a selected destination
    '''
    def macos_x86(source, dest):
        sysrsync.run(source=source, destination=dest)
        if os.path.isfile(dest):
            print(f"Function succeeded, file located at: ", dest)

    def freebsd(source, dest):
        sysrsync.run(source=source, destination=dest)
        if os.path.file(dest):
            print(f"Function succeeded, file located at: ", dest)