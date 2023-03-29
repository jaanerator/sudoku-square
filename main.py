from datetime import datetime
from sudoku.solver import SquareSudokuSolver


if __name__ == '__main__':
    data = [[None, 2, None, 5, None, 1, None, 9, None],
            [8, None, None, 2, None, 3, None, None, 6],
            [None, 3, None, None, 6, None, None, 7, None],
            [None, None, 1, None, None, None, 6, None, None],
            [5, 4, None, None, None, None, None, 1, 9],
            [None, None, 2, None, None, None, 7, None, None],
            [None, 9, None, None, 3, None, None, 8, None],
            [2, None, None, 8, None, 4, None, None, 7],
            [None, 1, None, 9, None, 7, None, 6, None]]

    start = datetime.now()
    try:
        solver = SquareSudokuSolver(data, 3)
        solver.solve()
        validity = True
    except ValueError:
        validity = False
    except Exception as e:
        validity = False
        print(e)
    end = datetime.now()
    print('-' * 28)
    print('Result:')
    print(solver.mat_obj if validity else None)
    print('Statistic:')
    print('    total time : {:>8.3f} ms'.format((end - start).microseconds / 1000))
    print('    validity   : {!s:>11}'.format(validity))
    print('-' * 28)
    # print(solver.numbers_trace)
