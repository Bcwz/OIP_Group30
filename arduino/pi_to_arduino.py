#!/usr/bin/env python3
import serial
import time
    
def send_start():
    signal = 1
    ser.write(str(signal).encode('utf-8'))
    print("Sending signal " + str(signal) + " to Arduino.")
    
def send_pause():
    signal = 0
    ser.write(str(signal).encode('utf-8'))
    print("Sending signal " + str(signal) + " to Arduino.")
    
def read_signal():
    received_signal = ser.readline().decode('utf-8').rstrip()
    print(received_signal)
    if(received_signal =='a'):
        print('received signal from arduino')


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        command = input("insert command. \n")
        if ser.in_waiting > 0:
            read_signal()
        elif (command == 'start'):
            send_start()
            time.sleep(2)
        elif(command =='stop'):
            send_pause()
            time.sleep(2)
        else:
            print("Wrong command")
    
