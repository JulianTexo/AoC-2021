FILENAME = './inputs/04/input.txt'

def get_input() -> list:
    with open(FILENAME, ) as file:
        data =[line.strip() for line in file.readlines()]
    return data

def checkboards(markup_boards, boards, current) -> bool:
    for board in markup_boards:
        for line in board:
            if False not in line:
                
                
    

def part_1():
    data = get_input()
    input_str = data[0]
    boards = []
    markup = []
    row = []
    for line in data[1:]:
        if line == '':
            boards.append(row)
            row.clear()
        else:
            row.append(line)
    for board in boards:
        markup_board = []
        for line in board:
            markup_board.append([False, False, False, False, False])
        markup.append(markup_board)
        markup_board.clear()
    for x in range(len(input_str)):
        for board in boards:
            for line in board:
                if input_str[x] in line:
                    markup_board[boards.index(board)][line.index(input_str[x])] == True
        checkboards(markup_board, boards, input_str[x])    

if __name__ == "__main__":
    part_1()