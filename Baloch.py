import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/FhzbKR6VpU937CcL1FcDTq')
fbd=platform.architecture()[0]
if fbd=="32bit":
    __import__("B2")
elif fbd=="64bit":
    __import__("B2")
