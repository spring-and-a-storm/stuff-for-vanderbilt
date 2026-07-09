0.00000000003717049790   #232 mev, optimal
0.00000000002628350999   #164 mev, optimal / root2
0.00000000004502116341   #281 mev, maximum
0.00000000003183476857   #199 mev, maximum / root2


import math

mass = 0.00000000000000000000000008291
ke = float(input("Kinetic energy in Joules: "))

vsquared = (2 * ke) / mass
velocity = math.sqrt(vsquared)

sol = 299792458
percent = (velocity / sol) * 100

print(velocity)
print(f"{percent}% of the speed of light")