#time_string(15, 38, '24') returns '15:38'
#time_string(8, 3, '24') returns '08:03'
#time_string(0, 5 '24') returns '00:05'
#time_string(11, 15, '12') returns '11:15am'
#time_string(0, 7, '12') returns '12:07am'
#time_string(12, 46, '12') returns '12:46pm'
#time_string(13, 10, '12') returns '1:10pm'
#time_string(19, 02, '12') returns '7:02pm'

def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
                 
    elif time_format == '12':
        if hours >=12:
            hours -= 12
            hours = hours
            idk = 'PM'
        else:
            hours = hours
            idk = 'AM'
        return f"{hours}:{minutes:02d}{idk}"
print(time_string(15, 38, '24'))  # 15:38
print(time_string(8, 3, '24'))    # 08:03
print(time_string(0, 5, '24'))    # 00:05
print(time_string(11, 15, '12'))  # 11:15am
print(time_string(0, 7, '12'))    # 12:07am
print(time_string(7, 30, '12'))   # 7:30am
print(time_string(12, 46, '12'))  # 12:46pm
print(time_string(13, 10, '12'))  # 1:10pm
print(time_string(19, 2, '12'))   # 7:02pm
      