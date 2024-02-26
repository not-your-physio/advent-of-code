adventofcode1docpath = "day-01.txt"
print(adventofcode1docpath)

with open(adventofcode1docpath, 'r') as file:
    originalinput = ''.join(file.readlines()).strip()

chunks = originalinput.split(" ")
print(chunks)

def getchunknumbers(chunk):
    numbers = []
    for character in chunk:
        if character.isdigit():
            numbers.append(int(character))
    return numbers
    

def sumchunknumbers(numbers):
    return numbers[0]*10 + numbers[-1]

total = 0
for chunk in chunks: total += (sumchunknumbers(getchunknumbers(chunk)))
print(total)
