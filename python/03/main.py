import re

FILENAME = './inputs/03/input.txt'

def get_input() -> list:
    with open(FILENAME, ) as file:
        data =[line.strip() for line in file.readlines()]
    return data

def least(num_1, num_2) -> bool:
    if num_1 < num_2:
        return True
    elif num_1 == num_2:
        return True
    else:
        return False
    
def most(num_1, num_2) -> bool:
    if num_2 < num_1:
        return True
    elif num_1 == num_2:
        return False
    else:
        return False

def get_rates(bin_str, fun) -> str:
    result = ''
    for x in range(len(bin_str[0])):
        count_1 = 0
        count_0 = 0
        for line in bin_str:
            if line[x] == '0':
                count_0 += 1
            else:
                count_1 += 1
        if fun(count_0, count_1):
            result += '1'
        else:
            result += '0'
    return result

def get_ratings(input, fun) -> str:
    result = ''
    for x in range(len(input[0])):
        result_at_current = get_rates([line[x] for line in input], fun)
        result += result_at_current
        input = [line for line in input if line.startswith(result)]
        if len(input) == 1:
            return input[0]            
            
            

def part_1():
    data = get_input()
    gamma_rate = int(get_rates(data, least), 2)
    epsilon_rate = int(get_rates(data, most), 2)
    print(gamma_rate * epsilon_rate)
    
def part_2():
    data = get_input()
    oxygen_rating = int(get_ratings(data, least), 2)
    scrubber_rating = int(get_ratings(data, most), 2)
    print(oxygen_rating, scrubber_rating)
    print(oxygen_rating * scrubber_rating)
    

if __name__ == "__main__":
    #part_1()
    part_2()