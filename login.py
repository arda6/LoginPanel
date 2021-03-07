import random
from colorama import Fore, Back, Style, init
import questionary
init(autoreset=True)
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
    print(Fore.BLUE + "Login Successful")
    print(Style.RESET_ALL)
else:
    print(Fore.RED + "Login Unsuccessful")