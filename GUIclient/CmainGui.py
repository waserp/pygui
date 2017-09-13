import tkinter
import matplotlib.pyplot as plt
import zmq
import threading
#import Queue

class CmainGUI:
    def __init__(self, top):
        self.Bt1 = tkinter.Button(top, text ="Bal", command = lambda: self.helloCallBack(b"az"))
        self.Bt1.grid(row=0,column=0)
        self.Bt2 = tkinter.Button(top, text ="Hello", command =  lambda: self.helloCallBack(b"bz"))
        self.Bt2.grid(row=0,column=1)
        self.Bt3 = tkinter.Button(top, text ="Look", command =  lambda: self.helloCallBack(b"cz"))
        self.Bt3.grid(row=0,column=2)
        self.Lb1 = tkinter.Label(top, text="User Name")
        self.Lb1.grid(row=1,column=0,columnspan=2)
        self.En1 = tkinter.Entry(top, bd =5)
        self.En1.grid(row=1,column=2,columnspan=3)
        self.Lb2 = tkinter.Label(top, text="na")
        self.Lb2.grid(row=2,column=0,columnspan=4)

        self.context = zmq.Context()
        print("Connecting to hello world server")
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://localhost:5556")
        self.worker = threading.Thread(target= self.ReceiveThread)
        self.worker.start()

    def helloCallBack(self,parm):
        print ("bla",self.En1.get(),parm);
        res = self.socket.send(parm)
        print ("res=",res)

    def ReceiveThread(self):
        print("start endless loop")
        while True:
            msg = self.socket.recv()
            print ("message recevied:",msg)
#            self.Lb2.set(msg)
            self.Lb2['text'] = msg
