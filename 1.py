import subprocess
import keyboard

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def getClipboard():
    ret = subprocess.getoutput("powershell.exe -Command Get-Clipboard")
    return ret

def myfunc():
    print("Output")
def myfunc2():
    txt='Allowed as per history'
    cmd='echo '+txt.strip()+'|clip'
    subprocess.check_call(cmd, shell=True)
    return keyboard.press_and_release('ctrl+v')
    
while True:
    keyboard.add_hotkey('p', myfunc)
    keyboard.add_hotkey('ctrl+b', myfunc2)
    breakpoint()
# print(getClipboard())

##############################################################
s = 'abc:ppp sjsjsj'

print(s[s.index(':')+1:s.index(' ')])
