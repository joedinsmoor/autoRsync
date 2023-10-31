import sysrsync



'''
when windows is detected, autoRsync will call sysrsync and copy
a selected folder to a selected destination
'''
def windows():
    sysrsync.run(source='C:/', destination='X:/')

'''
when apple silicon based macos is detected, autoRsync will call sysrsync and copy
a selected folder to a selected destination
'''
def macos_x86():
    print("Starting for macos_x86\n\n")
    sysrsync.run(source='/home/', destination='/Volumes/')
    pass


'''
when linux is detected, autoRsync will call sysrsync and copy
a selected folder to a selected destination
'''
def linux_x86():
    sysrsync.run(source='/home/', destination='/Volumes/')
    pass

def linux_arm():
    sysrsync.run(source='/home/', destination='/Volumes/')
    pass


'''
when intel based macos is detected, autoRsync will call sysrsync and copy
a selected folder to a selected destination
'''
def macos_intel():
    sysrsync.run(source='/home/', destination='/Volumes/')
    pass

def freebsd():
    sysrsync.run(source='/home', destination='/Volumes/')