import calendar
cal = calendar.TextCalendar() # Create an instance
# class calendar.TextCalendar(firstweekday=0) firstweekday is Monday
# cal.pryear(2012) # What happens here?
# cal.prmonth(2012,3)
d = calendar.LocaleTextCalendar(6, "zh_TW.UTF-8")
d.pryear(2012)
print(calendar.isleap(2012))