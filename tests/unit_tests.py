import unittest
from resa.resa import *

class bookMeetingRoomUnitTests(unittest.TestCase):
  def test_small_room(self):
    self.assertEqual(bookMeetingRoom(5), Room.SMALL)
    self.assertEqual(bookMeetingRoom(15), Room.MEDIUM)
    

if __name__ == '__main__':
  unittest.main()
