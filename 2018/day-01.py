adventofcode181docpath = 'day-01.txt'

with open(adventofcode181docpath, 'r') as file:
    originalinput = ''.join(file.readlines()).strip()
    splitinput = originalinput.split()
print(splitinput)


frequency = 0
for value in splitinput:
    intvalue = int(value)
    frequency = frequency + intvalue
    
print(frequency)

##test = "+1 -5 +2"
##splittest = test.split()
##
##frequency = 0
##for value in splittest:
##    intvalue = int(value)
##    frequency = frequency + intvalue
##print(frequency)
