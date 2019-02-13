import math
G = 6.673*10**-11
g = 9.8
pi = math.pi

mass = [.025,.05,.075,.1,.125,.15,.175]
radius = .0125
friction_static = -1
friction_kinetic = -1
length = .032
modulus = -1
k = -1
l = [.001,.002,.003,.004,.004,.005,.006]
answer = []

def areaCirle(pi, radius):
    return pi*(radius**2)
area_circle = areaCirle(pi, radius)
print(area_circle)
def youngMod(mass,g,area_circle,l,length):
    return ((mass*g)/area_circle)/(l/length)

for i in range(0,len(l)):
    answer.append(youngMod(mass[i],g,area_circle,l[i],length))
average = sum(answer)/len(answer)

print(average)
print(answer)

#fg = mass*g
#delta_L = fg*length/(area_circle*modulus)