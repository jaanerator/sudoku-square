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

    try:
        solver = SquareSudokuSolver(data, 3)
        print(solver.n_steps)
        solver.keep_iterations()
        print(solver.n_steps)
    except AssertionError as e:
        print(e)
