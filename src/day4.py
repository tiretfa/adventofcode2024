f = open('data/day4_test.txt', 'r+')
table = []
for line in f.readlines():
    table.append(line.replace('\n', ''))

NB_OF_ROW = len(table)
NB_OF_COLUMN = len(table[0])

def one_star(table):
    xmas_count = 0

    for i in range(NB_OF_ROW):
        for j in range(NB_OF_COLUMN):
            if table[i][j] == 'X':
                if j + 3 < NB_OF_COLUMN and table[i][j:j+4] == 'XMAS':
                    xmas_count += 1
                if j - 3 >= 0 and table[i][j-3:j+1] == 'SAMX':
                    xmas_count += 1
                if i + 3 < NB_OF_ROW and table[i][j] + table[i+1][j]\
                    + table[i+2][j] + table[i+3][j] == 'XMAS':
                    xmas_count += 1
                if i - 3 >= 0 and table[i][j] + table[i-1][j] + table[i-2][j]\
                    + table[i-3][j] == 'XMAS':
                    xmas_count += 1
                if i + 3 < NB_OF_ROW and j + 3 < NB_OF_COLUMN and\
                    table[i][j] + table[i+1][j+1]+ table[i+2][j+2] + table[i+3][j+3] == 'XMAS':
                    xmas_count += 1
                if i - 3 >= 0 and j - 3 >= 0 and\
                    table[i][j] + table[i-1][j-1]+ table[i-2][j-2] + table[i-3][j-3] == 'XMAS':
                    xmas_count += 1
                if i - 3 >= 0 and j + 3 < NB_OF_COLUMN and\
                    table[i][j] + table[i-1][j+1]+ table[i-2][j+2] + table[i-3][j+3] == 'XMAS':
                    xmas_count += 1
                if i + 3 < NB_OF_ROW and j - 3 >= 0 and\
                    table[i][j] + table[i+1][j-1]+ table[i+2][j-2] + table[i+3][j-3] == 'XMAS':
                    xmas_count += 1
    return xmas_count

def two_star(table):
    xmas_count = 0
    for i in range(NB_OF_ROW):
        for j in range(NB_OF_COLUMN):
            if table[i][j] == 'A':
                if i - 1 >=0 and j -1 >=0 and i+1< NB_OF_ROW and j + 1 < NB_OF_COLUMN:
                    diag1 = table[i-1][j-1] + table[i][j] + table[i+1][j+1]
                    diag2 = table[i+1][j-1] + table[i][j] + table[i-1][j+1]
                    if (diag1 == 'MAS' or diag1 == 'SAM') and (diag2 == 'MAS' or diag2 == 'SAM'):
                        xmas_count += 1
    return xmas_count

print(one_star(table))
print(two_star(table))
