import socket
import os
import time
s=socket.socket()
try:
    print("seccessfull connected socket\n...................")
    g=s.connect(("localhost",501))
    k=socket.gethostname()


         #FALTU CODING
    for i in range(3):
        print("...")
        time.sleep(1)
    def clear_screen():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # for windows platfrom
            _ = os.system('cls')
    time.sleep(2)
    clear_screen()

        #FALTU SCREEN CLOSE

#CHAT screen+
    mess=" "
    print("connection seccessfull to DARK chat-room server '",k,"'\n")
    while True:
        msp = s.recv(10024)                                                 #recieve messags form serverclint
        print("~ ",msp.rstrip().decode())
        mess = input("                                             @ ")
        s.send(mess.encode())
        if mess=="~":
            break
#CLOSE CHAT SCREEN
    s.close()

#server busy!
except ConnectionRefusedError:
    print("\t\t Server Busy! can't responce the server ")
    s.close()

