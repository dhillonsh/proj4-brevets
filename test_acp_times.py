
from acp_times import *
import arrow

#Returns seconds from current time to when the checkpoint will open
def getOpenTime(control_dist_km, brevet_dist_km):
  nowTime = arrow.now()
  controlDist = open_time(control_dist_km, brevet_dist_km, nowTime)
  totalSeconds = arrow.get(controlDist).timestamp - nowTime.timestamp
  hours, minutes = divmod(totalSeconds, 60)
  print(hours)
  print(minutes)
  return 

#Returns seconds from current time to when the checkpoint will close
def getCloseTime(control_dist_km, brevet_dist_km):
  nowTime = arrow.now()
  controlDist = close_time(control_dist_km, brevet_dist_km, nowTime)
  return arrow.get(controlDist).timestamp - nowTime.timestamp

def test_standard200():
  assert getOpenTime(60, 200) == 6360 #1H46M
//  assert getOpenTime(120, 200) == 
