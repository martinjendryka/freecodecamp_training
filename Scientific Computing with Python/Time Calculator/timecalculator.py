#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:20:26 2024

@author: martinjendryka
"""

def add_time(start, duration,daystr=None):
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    start_len = len(start)
    dur_len = len(duration)
    daytime=start[-2:]
    hours_start=int(start[:start_len-6])
    minutes_start=int(start[-5:-3])
    hours_dur = int(duration[:dur_len-3])
    minutes_dur = int(duration[-2:])
    
    
    minutes_new = minutes_start + minutes_dur
    minutes_remainder = minutes_new%60
    add_hours = int(str(minutes_new/60)[0])
    hours_new = hours_start+ hours_dur + add_hours
          
    hours_remainder = hours_new%12
    if hours_remainder == 0:
        hours_remainder = 12
    add_days= str(hours_new/24)
    add_days = int(add_days[:add_days.index('.')])
    new_time_hours= hours_remainder
    new_time_minutes = str(minutes_remainder)
    
    if len(new_time_minutes)==1:
        new_time_minutes = '0' + new_time_minutes


    if hours_remainder < hours_start or hours_remainder==12:  
        if daytime=='AM':
            new_daytime ='PM' 
        else:
            new_daytime = 'AM'
            add_days=add_days+1
    else:
        new_daytime=daytime

    if daystr:
        day_idx = days.index(daystr.capitalize())
        nextday_idx = (day_idx+add_days)%7
        if add_days==1:
            new_time = f"{new_time_hours}:{new_time_minutes} {new_daytime}, {days[nextday_idx]} (next day)"
        elif add_days>1:
            new_time = f"{new_time_hours}:{new_time_minutes} {new_daytime}, {days[nextday_idx]} ({add_days} days later)"
        else:
            new_time = f"{new_time_hours}:{new_time_minutes} {new_daytime}, {days[nextday_idx]}"

        
        
    else:
        if add_days==1:
            new_time = f"{new_time_hours}:{new_time_minutes} {new_daytime} (next day)"
        elif add_days>1:
            new_time = f"{new_time_hours}:{new_time_minutes} {new_daytime} ({add_days} days later)"
        else:
            new_time = f"{new_time_hours}:{new_time_minutes} {new_daytime}"
            
    return new_time

start = '8:16 PM'
duration = '466:02' # duration to be added
print(add_time(start, duration))