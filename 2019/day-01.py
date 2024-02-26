adventofcode119docpath = "day-01.txt"


with open(adventofcode119docpath, 'r') as file:
    originalinput = ''.join(file.readlines()).strip()


import math

masses = originalinput.split()

def fuel_calculator(masses):
    masstotal = 0
    for mass in masses:
        massint = int(mass)
        mass_int = massint / 3
        masstotal += math.floor(mass_int - 2)
    return masstotal

def extrafuel_calculator(fuel):
    extrafuel = 0
    while fuel > 5:
        addedfuel = (fuel//3)-2
        extrafuel += addedfuel
        fuel = addedfuel
    return extrafuel

def all_fuel_calculator(masses):
    fueltotal = 0
    for mass in masses:
        massint = int(mass)
        mass_int = massint / 3
        fuelformass = math.floor(mass_int - 2)
        fueltotal += extrafuel_calculator(fuelformass) + fuelformass
    return fueltotal

print(all_fuel_calculator(masses))
print(fuel_calculator(masses))

print(extrafuel_calculator(10))
print(extrafuel_calculator(14))
print(extrafuel_calculator(1969))
print(extrafuel_calculator(100756))

