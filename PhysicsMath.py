import math
G = 6.673*10**-11
g = 9.8
pi = math.pi

mass1 = [.1,.2,.3,.4,.5,.6]
mass2 = [.025,.05,.075,.1,.125,.15,.175]
radius1 = .025
radius2 = .0125
friction_static = -1
friction_kinetic = -1
length1 = .05
length2 = .032
modulus = -1
k = -1
deltal1 = [.002,.006,.008,.010,.012,.014]
deltal2 = [.001,.002,.003,.004,.004,.005,.006]
answer = []

def areaCirle(pi, radius):
    return pi*(radius**2)
area_circle = areaCirle(pi, radius1)
print(area_circle)
def youngMod(mass,g,area_circle,deltal1,length):
    return ((mass*g)/area_circle)/(deltal1/length)

for i in range(0,len(deltal1)):
    answer.append(youngMod(mass1[i],g,area_circle,deltal1[i],length1))
average = sum(answer)/len(answer)

print(average)
print(answer)

#fg = mass*g
#delta_L = fg*length/(area_circle*modulus)
