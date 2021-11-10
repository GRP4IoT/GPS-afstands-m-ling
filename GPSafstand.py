import math

latA = 55.70636
lonA = 12.53955

latB = 55.70636
lonB = 12.53946

coordA = latA, lonA
coordB = latB, lonB

def afstand(coordA, coordB):
    coordA = latA, lonA
    coordB = latB, lonB
    R = 6372800
    
    phi1, phi2 = math.radians(latA), math.radians(latB)
    dphi = math.radians(latB - latA)
    dlambda = math.radians(lonB - lonA)
    
    a = math.sin(dphi/2)**2 + \
        math.cos(phi1) *math.cos(phi2)*math.sin(dlambda/2)**2
                        
    return 2*R*math.atan2(math.sqrt(a), math.sqrt(1-a))
    afstand(coordA, coordB)

klasse_coord1 = 55.70636, 12.53955
klasse_coord2 = 55.70636, 12.53946

distance = afstand(klasse_coord1, klasse_coord2)

print(distance)


