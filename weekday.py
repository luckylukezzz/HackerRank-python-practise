
m,d,y=list(map(int,input().split()))
import calendar
wd=calendar.weekday(y,m,d)
week=['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(week[wd])