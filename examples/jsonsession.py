>>> msg = b'{"event" : "measurement", "well" : "2", "data" : [1,5,3,2.7,4]}'
>>> newmsg = json.loads(msg.decode("utf-8"))
>>> ar = newmsg['data']
>>> print(ar[2])
3
>>> print(ar)
[1, 5, 3, 2.7, 4]



 bname = b"start"
 jsmsg=b'{"event : "button", "name" : "' + bname + b'"}'

