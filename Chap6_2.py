import sys

def test(did_pass):
    """Print the result of the test."""
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def day_name(num):
    week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    for i in range(len(week)):
        if num == i:
            return week[i]
        else: continue
    return None

def day_num(weekday):
    week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    for i in range(len(week)):
        if weekday == week[i]:
            return i
        else: continue
    return None

def day_add(weekday, delta):
    delta = delta % 7
    if not (day_num(weekday) or day_name(delta)):
        return None
    return day_name((day_num(weekday) + delta) % 7)

def test_suite():
    '''
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)
    '''
    '''
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")
    '''
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")
    '''
    test(day_add(42, "Monday") == None)
    test(day_add("Sunday", 'a') == None)
    '''
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")

test_suite()