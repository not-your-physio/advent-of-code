adventofcode120docpath = "day-01.txt"


with open(adventofcode120docpath, 'r') as file:
    originalinput = ''.join(file.readlines()).strip()

numbers = originalinput.split()



def tt_maker(numbers):
    pairnumber = []
    prevnumber = 0
    for number in numbers:
        intnumber = int(number)
        for othernumber in numbers:
            othernumberint = int(othernumber)
            for otherothernumber in numbers:
                otherothernumberint = int(otherothernumber)
                if intnumber + othernumberint + otherothernumberint == 2020:
                    pairnumber.append(intnumber)
                    pairnumber.append(othernumberint)
                    pairnumber.append(otherothernumberint)
            else: prevnumber = intnumber
    return pairnumber
       
print(tt_maker(numbers))    #within the loop, loop through the numbers again for something that matches

print(1067 * 691 * 262)


