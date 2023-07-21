from datetime import timedelta, datetime

time1 = input("Time in (00:00:00) format limit(23:59:59)")
speed = input("Speed in this (1.50) format limit(9.99)")

# for error checking of input if needed
'''
#time1 limit
if len(time1) == 8:
        conditions = (time1[0] in '012',time1[1] in '0123456789', # conditions for true input
                        time1[2] == ':',time1[3] in '012345',
                        time1[4] in '0123456789',time1[5] == ':',
                        time1[6] in '012345',time1[7] in '0123456789')
        if all(conditions):
            print("OK")

#speed limit
if len(speed) == 4: 
        conditions = (len(speed) == 4, speed[1] == '.', speed[0] in '0123456789', # conditions for true
                        speed[2] in '0123456789', speed[3] in '0123456789')
        if all(conditions):
              print("ok")
              '''

# main function/code


def Calculate_result_time_and_saved_time(time1, speed):
    original_total_seconds = (int(time1[0]+time1[1]) * 3600) + (
        int(time1[3]+time1[4]) * 60) + (int(time1[6]+time1[7]))
    calculated_result_seconds = float(
        original_total_seconds)/float(speed)  # result
    rounded_calculated_result_seconds = round(
        calculated_result_seconds, 0)  # removing decimal part
    result_time = timedelta(
        seconds=rounded_calculated_result_seconds)  # changing format
    datetime1 = datetime.strptime(time1, "%H:%M:%S")
    datetime2 = datetime.strptime(str(result_time), "%H:%M:%S")
    saved_time = datetime1 - datetime2  # subracting to find saved time
    return str(result_time), str(saved_time)


print(Calculate_result_time_and_saved_time(time1, speed))
