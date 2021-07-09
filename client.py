#!/usr/bin/python
import socket
import sys
import json
HOST, PORT = "10.7.0.220", 5555
data = " ".join(sys.argv[1:])
class client:
   def __init__(self,host,port):
     self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     self.sock.connect((host,port))
     #Receive the greeting string
     self.sockFile = self.sock.makefile()
     c=self.sockFile.readline();
   
   def do_cmd(self,obj):
     self.sock.sendall((json.dumps(obj)+"\n").encode("utf8"))
     res = self.sockFile.readline()
     res = json.loads(res)
     return res


