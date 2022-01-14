from array import array
import time
import pyb


class HUB:

    def __init__(self) -> None:
        self.can = pyb.CAN(1)
        self.can.init(pyb.CAN.NORMAL, extframe=False, prescaler=54,sjw=1, bs1=7, bs2=2, auto_restart=True)
        self.can.setfilter(0, self.can.MASK16, 0, (0, 0, 0, 0))
         
    @staticmethod
    def set_buff_with_values(size,*values):
        buff = bytearray(size)
        for i,val in zip(len(buff),values):
            buff[i] = val
        return buff

    @staticmethod
    def set_clean_buff(size):
        return bytearray(size), [0, 0, 0, memoryview(bytearray(size))]

    #translate old method to OOP(trial)
    def GetVer(self,id,size):
        self.can.send("\x00\x01",id)
        _ , lst = self.set_clean_buff(size)
        self.can.recv(0,lst)

        print("ID: ", lst[0])
        print("RTR: ", lst[1])
        print("FMI: ", lst[2])
        VerH = (lst[3][2] << 8) | (lst[3][3] & 0xff)
        print("VerH: ", VerH)
        VerL = (lst[3][4] << 8) | (lst[3][5] & 0xff)
        print("VerL: ", VerL)
        VerD = (lst[3][6] << 8) | (lst[3][7] & 0xff)
        print("VerD: ", VerD)



    # Check what is lst and how it is important to sending CAN 





