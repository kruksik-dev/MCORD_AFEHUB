import network
import _thread
import usocket
import ujson
import misc
import afedrv


BUFFER_SIZE = 1024
# Functions which process requests
def test_proper_connection(obj):
    return 'OK', obj[1] * obj[2]

def initialization(obj):
    if isinstance(obj[1], list):
        result = dict()
        for board in obj[1]:
            result[board] = misc.init(board)
        return ('OK', result)
    return ('OK', misc.init(obj[1]))

def turn_on(obj):
    result = misc.HVon(obj[1])
    return('OK', result)

def turn_off(obj):
    result = misc.HVoff(obj[1])
    return ('OK', result)

def setdac(obj):
    result = afedrv.SetDac(obj[1],obj[2],obj[3])
    return ('OK', result)

# Table of functions
func = {
    'init': initialization,
    'hvon': turn_on,
    'hvoff': turn_off,
    'setdac':setdac,
    'test':test_proper_connection,
}


class Ctlsrv():
    def __init__(self):
        # Start Ethernet
        self.lan = network.LAN()
        self.lan.active(1)
        # Start server
        self.srvthread = None
        self.runflag = False
        self.ip = ''
    
    def getip(self):
        self.ip = self.lan.ifconfig()[0]

    def __str__(self):
        self.getip()
        return 'AFE HUB %s' % (self.ip)

    @staticmethod
    def send_msg(cl, msg):
        cl.sendall((ujson.dumps(msg)).encode("utf8"))

    def srv_handle(self, port):
        
        addr = usocket.getaddrinfo('0.0.0.0', port)[0][-1]
        print(addr)
        s = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        s.setsockopt(usocket.SOL_SOCKET, usocket.SO_REUSEADDR, 1)
        s.bind(addr)
        print(s)
        s.listen(1)
        print('listening on', addr)
        while self.runflag:
            cl, addr = s.accept()
            print('client connected from', addr)
            self.send_msg(cl, 'Client connected with %s' % (self))
            while True:
                json = cl.recv(BUFFER_SIZE)
                if not json:
                    break
                try:
                    cmd = ujson.loads(json)
                    print(cmd)
                    res = func[cmd[0]](cmd)
                except Exception as e:
                    res = ('ERR', str(e))
                Ctlsrv.send_msg(cl, res)
            cl.close()

    def run(self, port):
        if self.srvthread:
            raise(Exception("Server already running"))
        self.runflag = True
        self.srvthread = _thread.start_new_thread(self.srv_handle, (port,))
        return

    def stop(self):
        self.runflag = False

        return


serv = Ctlsrv()
serv.run(5555)


