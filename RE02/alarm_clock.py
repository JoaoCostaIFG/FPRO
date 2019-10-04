#!/usr/bin/env python3

import datetime

now = datetime.datetime.now()
print("Now: " + now.strftime("%H:%M"))
# class datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
now = now + datetime.timedelta(0, 0, 0, 0, 30, 8)
print("Alarm: " + now.strftime("%H:%M"))