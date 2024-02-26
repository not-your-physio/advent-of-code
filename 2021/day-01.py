adventofcode121docpath = "day-01.txt"


with open(adventofcode121docpath, 'r') as file:
    originalinput = ''.join(file.readlines()).strip()

depths = originalinput.split()

print(depths)





def depth_increasing(depths):
    n = 0
    prev_depth = 0
    for depth in depths:
        depth_n = int(depth)
        if depth_n > prev_depth:
            prev_depth = depth_n
            n = n + 1
        else: prev_depth = depth_n
    return n - 1
    

print(depth_increasing(depths))

