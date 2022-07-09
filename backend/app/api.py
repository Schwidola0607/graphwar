from enum import Enum
class GraphWarAPI(Enum):
  join_room = 'join_room'
  room_error = 'room_error'
  room_feed = 'room_feed'
  room_ack = 'room_ack'