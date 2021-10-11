from valve import valve

offset = 0
pos = offset
idle = True
intake = valve("intake")
exhaust = valve("exhaust")

throttle = 10

while (idle):
    intake.open(throttle)
    waitTill(180)
    intake.close()
    waitTill(180)
    exhaust.open()
    waitTill(0)
    exhaust.close()




def waitTill(rotation):
    print("Crank is at 180")

def valveConfig(numOfCylinders):
    for i in range(numOfCylinders):
        valves.append()
        valves[i][0].append(valve("Air"))
        valves[i][1].append(valve("Exhaust"))
