from datetime import datetime
from sudoku.solver import SquareSudokuSolver


def main(data, n, verbose=1):
    # Time checker
    start = datetime.now()

    # Solve sudoku
    try:
        solver = SquareSudokuSolver(data, n)
        validity = solver.solve()
    except ValueError:
        print('ValueError occured: Check input matrix again')
        validity = False
    except Exception as e:
        print('Error occured: See the message below,\n', e)
        validity = False
    
    # Time checker
    end = datetime.now()
    elapsed = (end - start).microseconds / 1000

    # Result
    result_string = '-' * 30
    result_string += '\nResult:\n'
    if validity:
        result_string += solver.mat_obj.__str__()
    else:
        result_string += 'It failed to solve the sudoku,\n'
        result_string += 'check your input again.\n'
    result_string += 'Statistic:\n'
    result_string += '    total time : {:>8.3f} ms\n'.format(elapsed)
    result_string += '    validity   : {!s:>11}\n'.format(validity)
    result_string += '-' * 30
    if verbose == 1:
        print(result_string)
    return solver, result_string


if __name__ == '__main__':
    data = [[None, 8, None, None, None, 7, None, 5, None],
            [None, 1, None, 3, None, None, 6, None, None],
            [4, None, None, None, None, 8, 9, None, None],
            [None, 7, None, None, 2, None, None, 4, 5],
            [None, None, None, None, None, 1, None, 2, None],
            [None, None, None, 4, None, None, None, None, 1],
            [None, None, 2, None, 8, None, None, None, None],
            [None, None, 4, None, None, 9, None, None, None],
            [5, None, None, None, None, None, None, 6, 2]]
    # data = [[None, 2, None, 5, None, 1, None, 9, None],
    #         [8, None, None, 2, None, 3, None, None, 6],
    #         [None, 3, None, None, 6, None, None, 7, None],
    #         [None, None, 1, None, None, None, 6, None, None],
    #         [5, 4, None, None, None, None, None, 1, 9],
    #         [None, None, 2, None, None, None, 7, None, None],
    #         [None, 9, None, None, 3, None, None, 8, None],
    #         [2, None, None, 8, None, 4, None, None, 7],
    #         [None, 1, None, 9, None, 7, None, 6, None]]
    
    main(data, n=3, verbose=1)
