'''this .py file not for run it's only carry for backup beacuse development process stil in progress'''

'''note:
         also first run server_chat.py file on cmd using command " python server_chat.py"
              secound you run client1.py file on cmd using command "python client1.py"
              and also run both on cmd by using cmd partition  by one without intrupting after run server_chat.py file  
                                                                 ! Thank-you
          '''



















'''def student()  r=input("\nrollno: ")
    n=input("\nname  : ")
    c=input("\nclass : ")
    p=input("chake :")
    if r==p:
        print("your student")
        print(r,n,c)
#student()''''''
import sys
import os
import time
def clear():
    print("continue is working")
    time.sleep(3)

clear()'''
import os
import time
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
   # print out some text
print("The platform is: ", os.name)
print("big output\n"* 1)
# wait for 5 seconds to clear screen
n=input(":::::::::::",)
time.sleep(2)

# now call function we defined above
screen_clear()
print(n)