#!/usr/bin/python3

import zmq
import random
import sys
import time

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)
msg = b""
while True:
    socket.send(b"Server message to client3" + msg)
    msg = socket.recv()
    print (msg)
    time.sleep(1)
