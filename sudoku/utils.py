def check_squared_sudoku(mat, n):
    try:
        is_squared = len(mat) == n ** 2
        is_squared &= all([len(row) == n ** 2 for row in mat])
    except TypeError:
        is_squared = False
    except Exception as e:
        is_squared = False
        print(e)
    return is_squared


def check_numbers(mat):
    cnt = 0
    for row_wise in mat:
        for elem in row_wise:
            if elem is not None:
                cnt += 1
    return cnt
