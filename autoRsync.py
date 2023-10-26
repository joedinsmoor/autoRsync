import sysrsync
import os



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
    sysrsync.run(source='/home/', destination='/Volumes/')
    pass


'''
when linux is detected, autoRsync will call sysrsync and copy
a selected folder to a selected destination
'''
def linux():
    sysrsync.run(source='/home/', destination='/Volumes/')
    pass


'''
when intel based macos is detected, autoRsync will call sysrsync and copy
a selected folder to a selected destination
'''
def macos_intel():
    sysrsync.run(source='/home/', destination='/Volumes/')
    pass