# -*- coding: utf-8 -*-

import calendar

cal = calendar.Calendar(firstweekday = 0)

week_days = {
    "0": "Sunday",
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",    
}

for day in cal.iterweekdays():
    print(week_days.get(str(day)))


