import socket
import time
import os
print("\n     Error: No clients are connected to the server___________\n      note: After get clients connection process will auto start...........")


l=socket.gethostname()
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',501))
s.listen(3)
c,adrs=s.accept()
                  #Accept Connection


                  #FALTU CODING"
def clear_screen():
    print("connected............. to ",l)
    for i in range(3):
        print("..")
        time.sleep(0.50)
    time.sleep(1)
    print("\nconnection connected to 'dark server' address '",adrs,"'")
    c.send("wellcome to the Dark server chat-room''''''''\n   $ how can we help you  ".encode())
    time.sleep(1)
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')
clear_screen()
                 #FALTU CODING "CLOSE"


     #CHAT SCREEN
message=" "
print("....Darkweb secure chat connection available user connected''''''\n")
print("                                               @ wellcome to the Dark server chat-room''''\n                                                 $ how can we help you  ".rstrip())
while True:
    h=c.recv(15891)
    print("~ ",h.rstrip().decode())
    message=input("                                               @ ")
    c.send(message.encode())
    if message=="~":
        break


c.close()






