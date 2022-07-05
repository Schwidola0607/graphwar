from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, send

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "secret"
socketio = SocketIO(app)
print("executing app.py")

@socketio.on('message')
def handle_message(message):
    print("received message from client")
    send(message)

@app.route('/')
def hello_geek():
    print("printing hello h1")
    return '<h1>Hello from Flask & Docker</h1>'

@app.route('/test')
def test():
    return 'result'
if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0')
    print("starting backend")
    socketio.run(app)