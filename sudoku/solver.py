from .utils import check_squared_sudoku, check_numbers


class SquareSudokuSolver:

    """
    Class SquareSudokuSolver
    """

    def __init__(self, mat, n):
        assert check_squared_sudoku(mat, n), "InputError: Matrix Size is invalid"
        self.mat = mat
        self.n2 = n ** 2
        self.n_steps = check_numbers(mat)
        self.mat_candidates = [[None] * self.n2] * self.n2
        return

    def solve(self):
        return
    
    def one_iteration(self):
        for row in range(self.n2):
            for col in range(self.n2):
                if self.mat[row][col] is None:
                    candidates = self.draw_candidates(row, col)
                    if len(candidates) == 1:
                        self.mat[row][col] = candidates[0]
                        self.mat_candidates[row][col] = None
                        self.n_steps += 1
                    else:
                        self.mat_candidates[row][col] = candidates
        return
    
    def draw_candidates(self, row, col):
        # TODO : Rewrite Algorithm (needs only just one loop)
        neighbors = []
        neighbors += [self.mat[row][i] for i in range(self.n2)]
        neighbors += [self.mat[i][col] for i in range(self.n2)]
        sec_row = row // 3 * 3
        sec_col = col // 3 * 3
        neighbors += [self.mat[i][j] for i in range(sec_row, sec_row + 3) for j in range(sec_col, sec_col + 3)]

        candidates = []
        for cand in range(1, 10):
            if cand not in neighbors:
                candidates.append(cand)
        return candidates
    
    def keep_iterations(self):
        before = self.n_steps
        stop = False
        while not stop:
            self.one_iteration()
            stop = before == self.n_steps
            before = self.n_steps
        return
    
    # @property
    # def mat(self):
    #     return self._mat
    
    # @mat.setter
    # def mat(self, mat):
    #     self._mat = mat
    #     return


# class Sudoku:
#     def __init__(self, mat, mode='plot'):
#         # Intro
#         print('-' * 50)
#         start = datetime.now()

#         # Input
#         self.mat_solved = np.array(mat)
#         self.mat_raw = np.array(mat)

#         # Setter
#         self.mat_save = []
#         self.numbers_save = []
#         self.n_errors = 0
#         self.numbers_list = []

#         # Output
#         self.solver()

#         # Outro
#         end = datetime.now()
#         print('A Result of SUDOKU_SOLVER')
#         print('\t total time\t\t: %2.3f sec' % (end - start).total_seconds())
#         print('\t # of backing\t: %d times' % self.n_errors)
#         print('\t completeness\t: %s' % str(self.check_completeness()))
#         print('-' * 50)

#         return

#     def solver(self):
#         self.keep_iterations()
#         self.numbers_list.append(self.numbers)
#         list_candidates = np.concatenate(self.mat_candidates, axis=0).tolist()
#         list_candidates.sort(key=sort_candidates)
#         list_candidate = list_candidates[0]
#         if self.numbers == 81:
#             return True
#         elif len(list_candidate[2]) == 0:
#             self.mat_solved = self.mat_save.pop()
#             self.numbers = self.numbers_save.pop()
#             self.n_errors += 1
#             return False
#         else:
#             self.mat_save.append(self.mat_solved.copy())
#             self.numbers_save.append(self.numbers)

#         for trial in list_candidate[2]:
#             self.mat_solved[list_candidate[0], list_candidate[1]] = trial
#             self.mat_candidates[list_candidate[0], list_candidate[1]] = None
#             self.numbers += 1
#             sub_solver = self.solver()
#             if sub_solver:
#                 return True

#     def check_completeness(self):
#         standard = [i for i in range(1, 10)]
#         for idx in range(9):
#             row = self.mat_solved[idx, :].tolist()
#             row.sort()
#             col = self.mat_solved[:, idx].tolist()
#             col.sort()
#             if row != standard or col != standard:
#                 return False
#         for row_sec in range(0, 9, 3):
#             for col_sec in range(0, 9, 3):
#                 line = []
#                 for i in range(3):
#                     line += self.mat_solved[row_sec + i, col_sec:col_sec + 3].tolist()
#                 line.sort()
#                 if line != standard:
#                     return False
#         return True
