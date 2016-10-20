
from acp_times import *
import arrow

#Returns seconds from current time to when the checkpoint will open
def getOpenTime(control_dist_km, brevet_dist_km):
  nowTime = arrow.now()
  controlDist = open_time(control_dist_km, brevet_dist_km, nowTime)
  totalSeconds = arrow.get(controlDist).timestamp - nowTime.timestamp
  hours, remainder = divmod(totalSeconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  return str(hours) + 'H' + str(minutes)

#Returns seconds from current time to when the checkpoint will close
def getCloseTime(control_dist_km, brevet_dist_km):
  nowTime = arrow.now()
  controlDist = close_time(control_dist_km, brevet_dist_km, nowTime)
  totalSeconds = arrow.get(controlDist).timestamp - nowTime.timestamp
  hours, remainder = divmod(totalSeconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  return str(hours) + 'H' + str(minutes)

def test_standard200():
  assert getOpenTime(60, 200) == '1H46'
  assert getOpenTime(120, 200) == '3H32'
  assert getOpenTime(175, 200) == '5H09'
  assert getOpenTime(200, 200) == '5H53'
