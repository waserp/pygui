import tkinter
import matplotlib.pyplot as plt
import zmq
import sys
import time
import threading
#import Queue
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class CmainGUI:
    def __init__(self, top):
        self.root=top
        self.Bt1 = tkinter.Button(top, text ="Bal", command = lambda: self.helloCallBack(b"bal"))
        self.Bt1.grid(row=0,column=0)
        self.Bt2 = tkinter.Button(top, text ="Hello", command =  lambda: self.helloCallBack(b"hello"))
        self.Bt2.grid(row=0,column=1)
        self.Bt3 = tkinter.Button(top, text ="Look", command =  lambda: self.helloCallBack(b"look"))
        self.Bt3.grid(row=0,column=2)
        self.Bt3 = tkinter.Button(top, text ="Exit", command =  self.ExitCallBack)
        self.Bt3.grid(row=0,column=3)
        self.Lb1 = tkinter.Label(top, text="User Name")
        self.Lb1.grid(row=1,column=0,columnspan=2)
        self.En1 = tkinter.Entry(top, bd =5)
        self.En1.grid(row=1,column=2,columnspan=3)
        self.Lb2 = tkinter.Label(top, text="na")
        self.Lb2.grid(row=2,column=0,columnspan=4)

        f = Figure(figsize=(5,5), dpi=100)
        self.line = f.add_subplot(111)
        self.line.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        self.line.grid(True)
        self.canvas = FigureCanvasTkAgg(f, master=top)
        self.canvas.show()
        self.canvas.get_tk_widget().grid(row=3,column=0,columnspan=10,rowspan=10)

        self.context = zmq.Context()
        print("Connecting to hello world server")
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://localhost:5556")

        self.root.after(100,self.Poller)

    def ExitCallBack(self):
        self.workerthreadFlag = False
        #res = self.socket.send(b"by")
        #self.socket.close()
        #self.context.term()
        sys.exit()
#        self.root.destroy()



    def helloCallBack(self,parm):
        print ("bla",self.En1.get(),parm);
        jsmsg=b'{"event : "button", "name" : "' + parm + b'"}'
        res = self.socket.send(jsmsg)
        print ("res=",res)


    def Poller(self):
        self.root.after(100,self.Poller)
        try:
            while True :
                msg = self.socket.recv(flags=zmq.NOBLOCK)
                self.Lb2['text'] = msg
                print(b"mesg rec : ", msg)
                self.line.plot([1,2,3,4,5,6,7,8],[8,7,5,3,8,9,3,5])
                self.canvas.draw()
        except zmq.Again:
            #No messages waiting to be processed
            pass

