
from acp_times import *
import arrow

#Returns seconds from current time to when the checkpoint will open
def getOpenTime(control_dist_km, brevet_dist_km):
  nowTime = arrow.now()
  controlDist = open_time(control_dist_km, brevet_dist_km, nowTime)
  totalSeconds = arrow.get(controlDist).timestamp - nowTime.timestamp
  hours, remainder = divmod(totalSeconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  return str(hours) + 'H' + '{0:02d}'.format(minutes)

#Returns seconds from current time to when the checkpoint will close
def getCloseTime(control_dist_km, brevet_dist_km):
  nowTime = arrow.now()
  controlDist = close_time(control_dist_km, brevet_dist_km, nowTime)
  totalSeconds = arrow.get(controlDist).timestamp - nowTime.timestamp
  hours, remainder = divmod(totalSeconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  return str(hours) + 'H' + '{0:02d}'.format(minutes)

def test_standard200():
  assert getOpenTime(60, 200) == '1H46'
  assert getOpenTime(120, 200) == '3H32'
  assert getOpenTime(175, 200) == '5H09'
  assert getOpenTime(200, 200) == '5H53'

  assert getCloseTime(60, 200) == '4H00'
  assert getCloseTime(120, 200) == '8H00'
  assert getCloseTime(175, 200) == '11H40'
  assert getCloseTime(200, 200) == '13H30'
  
def test_individuals():
  assert getOpenTime(350, 400) == '10H34'
  
  assert getOpenTime(550, 600) == '17H08'
  assert getCloseTime(550, 600) == '36H40'
  assert getCloseTime(600, 600) == '40H00'
  
  assert getOpenTime(890, 1000) == '65H23'
  assert getCloseTime(890, 1000) == '29H09'
  
  assert getOpenTime(0, 200) == '1H00'
