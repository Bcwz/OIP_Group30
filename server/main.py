import eventlet
import socketio

import sys
import Adafruit_DHT

import Constants

from Utils import *
import random

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


def set_state(new_state) -> None:
    global state
    state = new_state
    sio.emit(Constants.STATE, state, room=clients)


def get_humidity() -> str:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    return str(humidity)


def get_temperature() -> str:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    return str(temperature)


def wash() -> None:
    # Insert command to start washing here
    log("washing")
    set_state(Constants.WASHING)


def dry() -> None:
    # Insert command to start drying here
    log("drying")
    set_state(Constants.DRYING)


def start_cleaning() -> None:
    log("start_cleaning")
    wash()
    dry()


def stop_cleaning() -> None:
    log("stop_cleaning")
    set_state(Constants.STOP)
    pass


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
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)
