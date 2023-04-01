from copy import deepcopy
from .mat import SudokuMatrix


class SquareSudokuSolver:

    """
    Class SquareSudokuSolver
    """

    def __init__(self, mat, n):
        self.mat_obj = SudokuMatrix(mat, n)
        self.mat_candidates = [[None for col in range(self.mat_obj.n2)] for row in range(self.mat_obj.n2)]
        self.min_cands_row = None
        self.min_cands_col = None
        self.numbers_trace = [self.mat_obj.numbers]
        self.mat_saved = []
        return
    
    def solve(self):
        solve_result = self.run()
        self.min_cands_row = None
        self.min_cands_col = None
        self.mat_saved = []
        return solve_result
    
    def run(self):
        self.keep_iterations()
        self.numbers_trace.append(self.mat_obj.numbers)

        if self.mat_obj.numbers == self.mat_obj.n2 ** 2:
            result = True
        else:
            row = self.min_cands_row
            col = self.min_cands_col
            tracks = self.mat_candidates[row][col]
            if len(tracks) > 0:
                self.mat_saved.append((deepcopy(self.mat_obj), deepcopy(self.mat_candidates)))
                for alter in tracks:
                    self.mat_obj.insert(row, col, alter)
                    self.mat_candidates[row][col] = None
                    result = self.run()
                    if result:
                        break
            elif len(self.mat_saved) == 0:
                result = False
            else:
                result = False
                self.mat_obj, self.mat_candidates = self.mat_saved.pop()
                self.numbers_trace.pop()
        return result
    
    def keep_iterations(self):
        before = self.mat_obj.numbers
        stop = False
        while not stop:
            self.one_iteration()
            stop = before == self.mat_obj.numbers
            before = self.mat_obj.numbers
        return
    
    def one_iteration(self):
        len_cands_min = float('inf')
        for row in range(self.mat_obj.n2):
            for col in range(self.mat_obj.n2):
                candidates = self.mat_obj.get_candidates(row, col)
                if candidates is None:
                    pass
                elif len(candidates) == 1:
                    self.mat_obj.insert(row, col, list(candidates)[0])
                    self.mat_candidates[row][col] = None
                else:
                    self.mat_candidates[row][col] = candidates
                    len_cands = len(candidates)
                    if len_cands < len_cands_min:
                        self.min_cands_row = row
                        self.min_cands_col = col
                        len_cands_min = len_cands
        return
