import os
sudoPassword = "ABC07112005Lnmb"

def runXampp():
    command = '/opt/lampp/lampp start'
    p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
def stopXampp():
    command = '/opt/lampp/lampp stop'
    p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
def runPino():
    command = 'python3 /home/lumi/Project-Absensi/Python-Bot-Absensi/Pino/Pino.py'
    p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))