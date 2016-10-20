
from acp_times import *
import arrow

def test_standard200():
  assert 1 == 1
  print(arrow.now().timestamp)
  print(open_time(60,200,arrow.now()))
