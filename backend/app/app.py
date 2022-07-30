from flask import Flask, request, session
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit, join_room, leave_room, close_room
import Room
import User
from api import GraphWarAPI
import os.path
import json

with open(os.path.dirname(__file__) + "/../messages/message_en.json", "r") as f:
  message = json.load(f)

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "secret"
socketio = SocketIO(app)
print("executing app.py")
rooms = {}

def join(room_code, name):
  """
    wrapper around join_room from flask_socketIO
  """
  rooms[room_code].add_user(name, request.id)
  join_room(room_code)
  send(GraphWarAPI.room_ack)
  emit(GraphWarAPI.room_feed, message['room_join'] % name, to=room_code)
  emit(GraphWarAPI.update_user_list, rooms[room_code].get_user_list(), to=room_code)


@socketio.on('message')
def handle_message(message):
  print("received message from client")
  send(message)

@socketio.on(GraphWarAPI.join_room)
def join_room(data):
  room_code = data['room_code']
  name = data['name']
  action = data['action']
  session['name'] = name
  session['room'] = room_code
  
  if action == 'join_room':
    if room_code not in rooms:
      emit(GraphWarAPI.room_error, message['room_does_not_exist'])
    else:
      if rooms[room_code].contains_user(name):
        emit(GraphWarAPI.room_error, message['name_exists'])
      else:
        join(room_code, name)
        print(f'User {name} {request.id} just joined the game')
  else:
    if room_code in rooms:
      emit(GraphWarAPI.room_error, message['room_exists'])
    else:
      rooms[room_code] = Room()
      join(room_code, name)
      print(f'User {name} {request.id} just created the game')
            

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

