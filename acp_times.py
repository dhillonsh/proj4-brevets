"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
from datetime import tzinfo
#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#

timeGrid = [
    (200, 15, 34),
    (200, 15, 32),
    (200, 15, 30),
    (400, 11.428, 28)
]
    
def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    global timeGrid
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    
    #Limit the last checkpoint's opening time to use the brevet distance
    if control_dist_km > brevet_dist_km:
        control_dist_km = brevet_dist_km
    
    openingTime = 0
    for distance in timeGrid:
        if control_dist_km > distance[0]:
            control_dist_km -= distance[0]
            openingTime += distance[0] / distance[2]
        else:
            openingTime += control_dist_km / distance[2]
            break
    openingTime_Hours = int(openingTime)
    openingTime_Minutes = round((openingTime - openingTime_Hours) * 60) 

    return arrow.get(brevet_start_time, "YYYY-M-D HH:mm", tzinfo=tz.tzlocal()).replace(hours=+openingTime_Hours, minutes=+openingTime_Minutes).isoformat()

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    global timeGrid
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    
    #checkpointSwitch: 0 = checkpoint 0, 2 = last checkpoint, 1 = every other checkpoint
    if control_dist_km == 0:
        checkpointSwitch = 0
    elif control_dist_km >= brevet_dist_km:
        checkpointSwitch = 2
    else:
        checkpointSwitch = 1

    closingTime = 0
    for distance in timeGrid:
        if control_dist_km >= distance[0]:
            control_dist_km -= distance[0]
            closingTime += distance[0] / distance[1]
        else:
            if checkpointSwitch != 2:
                closingTime += control_dist_km / distance[1]
            break
            
    #The closing time for checkpoint 1, at 0m., is 1 hour
    if checkpointSwitch == 0:
        closingTime_Hours = 1
        closingTime_Minutes = 0
        
    #Fixed closing times if the checkpoint is past the brevet distance
    elif checkpointSwitch == 2:
        fixedClosings = {200: (13, 30), 300: (20, 0), 400: (27, 0), 600: (40, 0), 1000: (75, 0) }
        closingTime_Hours, closingTime_Minutes = fixedClosings[brevet_dist_km]
    else:
        closingTime_Hours = int(closingTime)
        closingTime_Minutes = round((closingTime - closingTime_Hours) * 60)

    return arrow.get(brevet_start_time).replace(hours=+closingTime_Hours, minutes=+closingTime_Minutes).isoformat()
