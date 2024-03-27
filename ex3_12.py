travelDistance = float(input("Enter with the travel distance(KM): "))
speed = float(input("Enter with the speed  of the travel(KM/H): "))

timeTravel = travelDistance / speed
hour = int(timeTravel)
minute = timeTravel - hour
mintRe = str(timeTravel)
if timeTravel%2 == 0:
    print(f"Travel time will be: {timeTravel}Hr")
else:
    print(f'Travel time will be: {hour} Hora(s) e {mintRe[:1]} minutos')