import math

mass = float(input("Enter mass in kilograms: "))
radius = float(input("Enter radius in meters: "))
magnet = float(input("Enter the magnetic force in Teslas: "))
charge = float(input("Enter the charge in Coulumbs: "))
speedoflight = 299792458
on = 1

while on == 1:
    speed = float((radius * charge * magnet) / mass)
    lightpercent = (speed / speedoflight) * 100

    if lightpercent >= 20:
        print(f"The Lorentz factor is necessary for this problem.")
        speed = ((radius * charge * magnet) / (math.sqrt((mass ** 2) + (((radius * charge * magnet) / speedoflight) ** 2))))
        print(f"Your new speed with the Lorentz factor is {speed}.")
    lightpercent = (speed / speedoflight) * 100
    print(f"The speed is {speed} m/s. This is {lightpercent}% of the speed of light.")
    on = int(input("Type 1 to go again with a new charge, 0 to stop: "))
    charge = float(input("Enter the charge in Coulumbs: "))