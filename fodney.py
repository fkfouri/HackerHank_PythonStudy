



d = {}
d = dict()

d['rodney'] = []
d['1'] = {}
d['2'] = (1,2,'rodney')

d['rodney'] = (1,2,'rodney')



print(d)

#available drones
av = [drone for drone in drones if drone.id not in inMaintenanceDrones] 

res = sorted([drone.flightRange for drone in av], reverse = True)
dd = [item.id for item in av if item.flightRange in res[:requiredDrones]]

t = [1,2,3,4,5,6,7,8,9]

x = filter(lambda x: x>=5 , t)