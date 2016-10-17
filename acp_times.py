"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#


def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
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
    print(arrow.get(brevet_start_time).isoformat())
    timeGrid = [
        (200, 15, 34),
        (200, 15, 32),
        (200, 15, 30),
        (400, 11.428, 28)
    ]
    
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
    print(openingTime)
    print(openingTime_Hours, "H | ", openingTime_Minutes , "M")
    print(arrow.get(brevet_start_time).replace(hours=+openingTime_Hours, minutes=+openingTime_Minutes).isoformat())
    return arrow.get(brevet_start_time).replace(hours=+openingTime_Hours, minutes=+openingTime_Minutes).isoformat()

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
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
    return arrow.now().isoformat()


