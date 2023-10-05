#!/usr/bin/env python3
# http://weifan-tmm.blogspot.kr/2015/07/a-simple-turorial-for-python-c-inter.html
import sysv_ipc
import time

BUFF_SIZE = 16
TYPE_STRING = 1

if __name__ == '__main__':
    msg_string = "sample string\0"
    
    try:
        while True:
          mq = sysv_ipc.MessageQueue(1234, sysv_ipc.IPC_CREAT)

          # string transmission
          mq.send(msg_string, True, type=TYPE_STRING)
          print(f"string sent: {msg_string}")

          time.sleep(5)

    except sysv_ipc.ExistentialError:
        print("ERROR: message queue creation failed")

