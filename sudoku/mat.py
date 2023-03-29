class SudokuMatrix:
    def __init__(self, mat, n):
        self.mat = mat
        self.n = n
        self.n2 = n ** 2
        self.numbers = None
        self.rowwise_cands = None
        self.colwise_cands = None
        self.secwise_cands = None

        self.check_squared_sudoku()
        self.check_numbers()
        self.set_candidates()
        return
    
    def check_squared_sudoku(self):
        try:
            is_squared = len(self.mat) == self.n2
            is_squared &= all([len(row) == self.n2 for row in self.mat])
        except:
            is_squared = False
        if not is_squared:
            raise ValueError('An error occured while creating sudoku matrix object')
        return
    
    def check_numbers(self):
        numbers = 0
        for row_wise in self.mat:
            for elem in row_wise:
                if elem is not None:
                    numbers += 1
        self.numbers = numbers
        return
    
    def set_candidates(self):
        numbers_set = set(range(1, self.n2 + 1))
        rowwise_cands = []
        colwise_cands = []
        secwise_cands = []
        for i in range(self.n2):
            row_lb = i // self.n * self.n
            row_ub = row_lb + self.n
            col_lb = i % self.n * self.n
            col_ub = col_lb + self.n

            row_list = [cand for cand in self.mat[i] if cand is not None]
            col_list = [row_wise[i] for row_wise in self.mat if row_wise[i] is not None]
            sec_list = [cand for section in self.mat[row_lb:row_ub] for cand in section[col_lb:col_ub] if cand is not None]
            row_set = set(row_list)
            col_set = set(col_list)
            sec_set = set(sec_list)
            if len(row_list) != len(row_set) or len(col_list) != len(col_set) or len(sec_list) != len(sec_set):
                raise ValueError('An error occured while creating sudoku matrix object')
            rowwise_cands.append(numbers_set - row_set)
            colwise_cands.append(numbers_set - col_set)
            secwise_cands.append(numbers_set - sec_set)
        
        self.rowwise_cands = rowwise_cands
        self.colwise_cands = colwise_cands
        self.secwise_cands = secwise_cands
        return
    
    def get_candidates(self, row, col):
        elem = self.mat[row][col]
        if elem is not None:
            result = None
        else:
            row_cands = self.rowwise_cands[row]
            col_cands = self.colwise_cands[col]
            sec_cands = self.secwise_cands[row // self.n * self.n + col // self.n]
            result = row_cands & col_cands & sec_cands
        return result
    
    def insert(self, row, col, value):
        if self.mat[row][col] is None:
            self.numbers += 1
        self.mat[row][col] = value
        self.set_candidates()
        return
    
    def pop(self, row, col):

        """It is not used by SquareSudokuSolver actually"""

        if self.mat[row][col] is not None:
            self.numbers -= 1
        self.mat[row][col] = None
        self.set_candidates()
        return
    
    def __str__(self):
        print_out = ''
        for i, row_wise in enumerate(self.mat):
            for j, elem in enumerate(row_wise):
                print_out += ' ' if elem is None else str(elem)
                print_out += '|' if j % self.n == self.n - 1 else ','
            print_out += '\n'
            print_out += '-' * 2 * self.n2 + '\n' if i % self.n == self.n - 1 else ''
        return print_out
    
    def __repr__(self):
        return f"<Sudoku matrix with size of {self.n2}>"
