caloriesdocument = "day-01.txt"
with open(caloriesdocument, 'r') as file:
    elfkcals = ''.join(file.readlines()).strip().split("  ")

print(elfkcals)

def inputtosnacks(elfkcals):
    snacks = []
    for elf in elfkcals:
        elfsnacks = elf.split(' ')
        snacks.append(elfsnacks)
    return snacks

print(inputtosnacks(elfkcals))

def snacktocalorietotal(snack):
    calorietotal = 0
    for numberstring in snack:
        number = int(numberstring)
        calorietotal += number
    return calorietotal



def snackstocalorietotals(snacks):
    calorietotals = []
    for snack in snacks:
        calorietotals.append(snacktocalorietotal(snack))
        
    return calorietotals

values = snackstocalorietotals(inputtosnacks(elfkcals))

sortedvalues = sorted(values)

print(sum(sortedvalues[-3:]))
        
