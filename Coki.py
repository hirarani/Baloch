import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/C3jiA8hbZLNHcEOmyYeYCG')
fbd=platform.architecture()[0]
if fbd=="32bit":
    __import__("coki")
elif fbd=="64bit":
    __import__("ckoi")
