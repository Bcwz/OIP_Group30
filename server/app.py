from flask import Flask,  Response
from camera import VideoCamera
from flask_cors import CORS
from Machine import Machine

from debug import log

pi_camera = VideoCamera(flip=False)  # flip pi camera if upside down.

machine = Machine()


def gen(camera):
    frame = camera.get_frame()
    return (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# Flask Stuff
app = Flask(__name__)
CORS(app)


@app.route("/state/")
def state():
    log("state")
    return machine.state


@app.route("/values/")
def values():
    log("values")
    # return {"length": dim.length, "width": dim.width, "height": dim.height, "volume": dim.volume()}
    return {"humidity": machine.get_humidity(), "temperature": machine.get_temperature()}


@app.route('/video_feed/')
def video_feed():
    log("video_feed")
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
