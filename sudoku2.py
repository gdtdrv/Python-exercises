def check_rows(input):
    for i,inner_list in enumerate(input):
        if len(set(input[i]))!=9:
            return False
        else:
            continue
    return True

def check_columns(input):
    vertical_row_matrix = [[None] * 9] * 9
    for i, sub_string in enumerate(input):
        for j, character in enumerate(input[i]):
            vertical_row_matrix[j][i] = input[i][j]

    for i, inner_list in enumerate(vertical_row_matrix):
        if len(set(vertical_row_matrix[i])) != 9:
            return False
        else:
            continue
    return True

def check_squares(input):
    for i, sub_string in enumerate(input):
        small_list = []
        for j, character in enumerate(input[i]):
            if j % 3 == 0 and i % 3 == 0:
                small_list = []
                for k in range(3):
                    for l in range(3):
                        small_list.append(input[i+k][j])
                        small_list.append(input[i][j+l])
                        small_list.append(input[i + k][j+l])
            else:
                continue
            if len(set(small_list)) != 9:
                return False
            else:
                continue
    return True

def sudoku(input):
    if check_squares(input) and check_rows(input) and check_squares(input):
        return True
    return False



if __name__ == "__main__":
    print(sudoku([
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9],
[1, 2, 3, 4, 5, 6, 7, 8, 9]
]))