
# The spreadsheet consists of rows of apparently-random numbers. To make sure
# the recovery process is on the right track, they need you to calculate the
# spreadsheet's checksum. For each row, determine the difference between the
# largest value and the smallest value; the checksum is the sum of all of these
# differences.

# It sounds like the goal is to find the only two numbers in each row where one
# evenly divides the other - that is, where the result of the division
# operation is a whole number. They would like you to find those numbers on
# each line, divide them, and add up each line's result.

def spreadsheet_checksum1(grid):
    return sum(max(line) - min(line) for line in grid)

def spreadsheet_checksum2(grid):
    return sum(a // b
               for line in grid
               for a in line
               for b in line
               if a != b and a % b == 0)

def test_2a_example(): assert spreadsheet_checksum1([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]) == 18
def test_2b_example(): assert spreadsheet_checksum2([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]) == 9

def test_2a_answer(day02_number_grid): assert spreadsheet_checksum1(day02_number_grid) == 34925
def test_2b_answer(day02_number_grid): assert spreadsheet_checksum2(day02_number_grid) == 221
