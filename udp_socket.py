import socket
import threading

protocol = socket.SOCK_DGRAM
address =  socket.AF_INET

conn = socket.socket(address,protocol)

guiip= "192.168.43.78"
guiport = 1234
cliip= "192.168.43.4"
cliport = 9001

conn.bind( (guiip, guiport))

def server():
    while True:
        data= conn.recvfrom(1024)
        clientip = data[1][0]
        datarecv = data[0].decode()
        print("\n"+clientip+" :"+ datarecv)
         

def client(cliip,cliport):
    while True:
        ans= input("Enter Message to send:\t")
        conn.sendto(ans.encode() ,(cliip,cliport))
 


x = threading.Thread(target= server)
x2 = threading.Thread(target= client, args=(cliip,cliport))
x.start()
x2.start()


