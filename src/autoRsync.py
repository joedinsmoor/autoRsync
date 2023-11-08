import sysrsync
import os


class autoRsync:
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
        print("Starting for macos_arm\n\n")
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