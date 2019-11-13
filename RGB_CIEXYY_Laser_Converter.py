import matplotlib.pyplot as plt
import math

img = plt.imread("CIE1931.png")
fig, ax = plt.subplots()
x = range(1)
ax.imshow(img, extent=[0, .8, 0, .9])

sR = int(input("Enter Red Value >> ")) #700nm
sG = int(input("Enter Green Value >> ")) #510nm
sB = int(input("Enter Blue Value >> "))  #440nm

#sR = 
#sG = 
#sB = 

prx = .709546 #primary red x
pry = .292408 #primary red y

pgx = .148
pgy = .81

pbx = .123326
pby = .0619733

var_R = ( sR / 255 )
var_G = ( sG / 255 )
var_B = ( sB / 255 )

if ( var_R > 0.04045 ):
    var_R = ( ( var_R + 0.055 ) / 1.055 ) ** 2.4
else:
    var_R = var_R / 12.92
    
if ( var_G > 0.04045 ):
    var_G = ( ( var_G + 0.055 ) / 1.055 ) ** 2.4
else:
    var_G = var_G / 12.92
    
if( var_B > 0.04045 ):
    var_B = ( ( var_B + 0.055 ) / 1.055 ) ** 2.4
else: var_B = var_B / 12.92

var_R = var_R * 100
var_G = var_G * 100
var_B = var_B * 100

X = var_R * 0.4124 + var_G * 0.3576 + var_B * 0.1805
Y = var_R * 0.2126 + var_G * 0.7152 + var_B * 0.0722
Z = var_R * 0.0193 + var_G * 0.1192 + var_B * 0.9505

var_x = X / ( X + Y + Z )
var_y = Y / ( X + Y + Z )

dist_r = math.sqrt((prx - var_x)**2 + (pry - var_y)**2) #distance from primary
dist_g = math.sqrt((pgx - var_x)**2 + (pgy - var_y)**2)
dist_b = math.sqrt((pbx - var_x)**2 + (pby - var_y)**2)

total_dist = dist_r + dist_g + dist_b

r_percent = round((100-(dist_r/total_dist)*100), 2)
g_percent = round((100-(dist_g/total_dist)*100), 2)
b_percent = round((100-(dist_b/total_dist)*100), 2)

plt.scatter([var_x], [var_y])
plt.scatter([prx], [pry]) 
plt.scatter([pgx], [pgy]) 
plt.scatter([pbx], [pby]) 

print("\nThe power percentages for each primary are:")
print("650nm Red:   " +str(r_percent) +"%")
print("532nm Green: " +str(g_percent) +"%")
print("473nm Blue:  " +str(b_percent) +"%")


plt.show()
