import calendar as c

date = [int(item) for item in input().split(' ')]
weekdays = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
print(weekdays[c.weekday(2009, date[1], date[0])])
