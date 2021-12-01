FILENAME = './inputs/01/input.txt'

def get_input() -> list[int]:
    with open(FILENAME, ) as file:
        data =[int(line.strip()) for line in file.readlines()]
    return data

def part_1():
    #load input data into a list
    data = get_input()

    #assume that the list isn't empty and load the first element into "previous"
    previous = data[0]

    #initialize a counter
    result = 0

    #iterate over the list (starting from the second element) and compare the current element to the previous one
    for row in data[1:-2]:
        if row > previous:
            result += 1
        previous = row
    print(result)

def part_2():
    #load input data into a list
    data = get_input()

    #assume that the list isn't empty and load the first elment into "previous"
    previous = data[0]

    #initialize a counter
    result = 0

    #iterate over the list, compare the sums of two sliding windows of size three
    for i in range(len(data)-3):
        sliding_window = data[i:(i+3)]
        sliding_window_next = data[(i+1):(i+4)]
        if sum(sliding_window_next) > sum(sliding_window):
            result += 1
    print(result)



if __name__ == '__main__':
    part_1()
    part_2()