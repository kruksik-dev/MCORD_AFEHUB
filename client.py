#!/usr/bin/python
import socket
import json
HOST, PORT = "10.7.0.220", 5555

class Client:
   def __init__(self,host,port):
     self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     self.sock.connect((host,port))
     res = self.sock.recv(1024)
     
     print(res.decode('utf-8'))

   def do_cmd(self,obj):
     self.sock.sendall((json.dumps(obj)).encode("utf8"))
     res = self.sock.recv(1024)
     if res:
         res = json.loads(res)
         return res
     else:
        pass
   
   def __del__(self):
     self.sock.close()

cli = Client(HOST, PORT)
