import sys
from resa.resa import *

participants = 0

if len(sys.argv) != 2:
  raise ValueError('Failed to parse command line')
else:
  participants = int(sys.argv[1])

print("Booking a meeting room for %d participants..." % participants)

room = bookMeetingRoom(participants)

if room == Room.REFUSE:
  print("Booking refused!")
else:
  print("%s room reserved." % room)
