import random
from colorama import Fore, Style, init
import questionary
from plyer import notification
init(autoreset=True)
title = "Cloud Software"
message = "Cloud Software Panel Signed In"
message2 = "Cloud Software Panel Could Sined In"
app_icon = (r"logo.ico")
uname1 = "admin"
password1 = "root"
print(Fore.WHITE + """"

               |--------------------------------|            
               |           ##########           |
               |          ############          |
               |         ##############         |
               |       ################         |
               |       ##################       |
               |      ####################      |
               |      Cloud Software Panel      |
               |      ####################      |
               |       ##################       |
               |        ################        |
               |         ##############         |
               |          ############          |
               |           ##########           |
               |--------------------------------|
""")
dogrulayici = str(random.randint(1,100))
str(dogrulayici)
uname = questionary.text("Cloud Software Username : ").ask()

password = questionary.password("Cloud Software Password : ").ask()

print("Verify Code :" + dogrulayici +"")

robot = questionary.text("Verify Code :").ask()

if password1 == password and uname1 == uname and robot == dogrulayici :
    notification.notify(title=title,
                        message=message,
                        app_icon=None,
                        timeout=8,
                        toast=False)
    print(Fore.BLUE + "Login Successful")
    print(Style.RESET_ALL)
else:
    notification.notify(title=title,
                        message=message2,
                        app_icon=None,
                        timeout=8,
                        toast=False)
    print(Fore.RED + "Login Unsuccessful")
