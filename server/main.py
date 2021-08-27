import eventlet
import socketio

import board
import adafruit_dht

# For limit switch
import RPi.GPIO as GPIO

# For pi to arduino imports
import serial
import time

import Constants

from Utils import *
import random

# GPIO Set Up
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Socketio Set Up
clients = "clients"
sio = socketio.Server(cors_allowed_origins='*')
# the index.html file hosted by eventlet is a dummy file
# it appears to be required to host some html file..
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


# Cleaning system Set Up
log("init machine")
state = Constants.STOP

# DHT Sensor Set Up
dhtDevice = adafruit_dht.DHT11(board.D4)

def set_state(new_state) -> None:
    global state
    state = new_state
    sio.emit(Constants.STATE, state, room=clients)

def door_is_closed() -> bool:
    if GPIO.input(18) == GPIO.HIGH:
        return False
    return True

def get_humidity() -> str:
    return dhtDevice.humidity


def get_temperature() -> str:
    return dhtDevice.temperature


def wash() -> None:
    # Insert command to start washing here
    log("wash")
    if state != Constants.STOP:
        set_state(Constants.WASHING)
        
        signal = 1
        ser.write(str(signal).encode('utf-8'))

        time.sleep(1)
    else:
        log("wash", "Stopping wash because of state")



def dry() -> None:
    # Insert command to start drying here
    log("dry")
    if state != Constants.STOP:
        set_state(Constants.DRYING)

        signal = 2
        ser.write(str(signal).encode('utf-8'))

        time.sleep(1)
    else:
        log("dry", "Stopping dry because of state")


def stop_cleaning() -> None:
    log("stop_cleaning")
    set_state(Constants.STOP)
    signal = 0
    ser.write(str(signal).encode('utf-8'))


def start_cleaning() -> None:
    log("start_cleaning")
    set_state(Constants.START)

    time = 0
    while (state != Constants.STOP and time < 60 and door_is_closed()):
        if time < 15:
            wash()
        elif time < 60:
            dry()
        time += 1
    stop_cleaning()


def handle_(instructions) -> None:
    print(instructions)
    if instructions == Constants.START:
        start_cleaning()
    elif instructions == Constants.STOP:
        stop_cleaning()
    elif instructions == Constants.DRY:
        dry()



# Start Listening
@sio.on('connect')
def connect(sid, environ) -> None:
    sio.enter_room(sid, clients)
    print('New Client: ', sid)
    sio.emit(Constants.STATE, state)


@sio.on(Constants.INSTRUCTION)
def new_instruction(sid, instructions):
    print(sid, 'instruction: ', instructions)
    handle_(instructions)


@sio.on('disconnect')
def disconnect(sid):
    sio.leave_room(sid, clients)
    print('Client disconnected: ', sid)


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)
