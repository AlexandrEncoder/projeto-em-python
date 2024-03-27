import math
day = int(input("Enter the day(s): "))
hour = int(input("Enter the hour(s): "))
minute = int(input("Enter the minute(s): "))
second = int(input("Enter the second(s): "))

daySecond = (((day*24)*60)*60)
hourSecond = ((hour*60)*60)
minuteSecond = minute*60
totalSecond = daySecond + hourSecond + minuteSecond + second

print('The total the number of second is ',totalSecond)