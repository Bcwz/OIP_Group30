from flask import Flask,  Response
import random
from camera import VideoCamera
from flask_cors import CORS

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.
def gen(camera):
    frame = camera.get_frame()
    return (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# Flask Stuff
app = Flask(__name__)
CORS(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route("/values/")
def values():
    # return {"length": dim.length, "width": dim.width, "height": dim.height, "volume": dim.volume()}
    return {"humidity": random.randint(0,100)}

@app.route('/video_feed/')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)