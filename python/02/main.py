FILENAME = './inputs/02/input.txt'

def get_input() -> list:
    with open(FILENAME, ) as file:
        data =[line.strip() for line in file.readlines()]
    return data

def part_1():
    #get input data
    data = get_input()
    
    #initialize horizontal position and depth
    horizontal = 0
    depth = 0
    
    #iterate over dictionary
    for line in data:
        direction, value = line.split()
        if direction == "forward":
            horizontal += int(value)
        elif direction == "down":
            depth += int(value)
        elif direction == "up":
            depth -= int(value)
    print(horizontal * depth)
    
def part_2():
    #get input data
    data = get_input()
    
    #initialize horizontal position, depth and aim
    horizontal = 0
    depth = 0
    aim = 0
    
    #iterate over data with different rules
    for line in data:
        direction, value = line.split()
        if direction == "forward":
            horizontal += int(value)
            depth += aim * int(value)
        elif direction == "down":
            aim += int(value)
        elif direction == "up":
            aim -= int(value)
            
    print(horizontal * depth)
    

if __name__ == "__main__":
    part_1()
    part_2()