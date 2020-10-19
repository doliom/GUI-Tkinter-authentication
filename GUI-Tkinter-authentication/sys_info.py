import platform
import getpass
from pathlib import Path
import win32com.client
import psutil
import win32api
import win32con
from win32api import GetSystemMetrics
import _pickle as pickle

def get_sys_info():
    #ім'я користувача
    username = getpass.getuser()
    print(username)

    #ім'я комп'ютера
    compname = platform.machine()
    print(compname)

    #шлях до папки з ОС
    path = Path('sys_info.py')
    print(path)

    #шлях до папки з системними файлами OC Windows
    objShell = win32com.client.Dispatch("WScript.Shell")
    allUserDocs = objShell.SpecialFolders("MyDocuments")
    print(allUserDocs)

    #кількість кнопок миші
    countMouseButtons = win32api.GetSystemMetrics(win32con.SM_CMOUSEBUTTONS)
    print(countMouseButtons)

    #ширина екрану
    widthScreen = GetSystemMetrics(0)
    print("width =", GetSystemMetrics(0))

    #об'єм пам'яті
    mem = psutil.virtual_memory()
    print(mem)

    sys_info = {
        'username': username,
        'compname': compname,
        'path': path,
        'allUserDocs': allUserDocs,
        'countMouseButtons': countMouseButtons,
        'wigthScreen': widthScreen,
        'mem': mem
    }
    return sys_info

def write_sys_info():
    sys_info = get_sys_info()
    path = Path('sys_info.txt')
    with open(path, 'w') as infofile:
        infofile.write(str(sys_info))

