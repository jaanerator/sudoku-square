import tkinter as tk
from datetime import datetime
from sudoku.solver import SquareSudokuSolver


class Application(tk.Frame):
    def __init__(self,
                 master,
                 master_title="Application",
                 icon=None,
                 window_size=(450, 400),
                 resizable=False):
        super().__init__(master)
        self.master = master

        self.window_width = None
        self.window_height = None

        # Create Apps
        self.master.title(master_title)
        if icon is not None:
            self.master.iconbitmap(icon)
        self.get_window_frame(window_size)
        self.master.resizable(resizable, resizable)
        return
    
    def get_window_frame(self, window_size):
        w, h = window_size
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.grid()

        self.window_width = int(w / 7)
        self.window_height = int(h / 7)
        return
    
    def get_subframe(self, ratio_width=1.0, ratio_height=1.0):
        return (int(self.window_width * ratio_width), int(self.window_height * ratio_height))


class SudokuAppWindow(Application):
    def __init__(self,
                 master,
                 master_title="Application",
                 icon=None,
                 window_size=(450, 400),
                 resizable=False):
        super().__init__(master, master_title, icon, window_size, resizable)

        self.size_label = None
        self.size_entry = None
        self.get_table_button = None
        self.mat_label = None
        self.mat_null = None
        self.result_label = None
        self.result_text = None
        self.size = None
        self.size2 = None
        self.mat_entry_list = None
        self.solve_button = None

        self.create_basic_widgets()
        return
    
    def create_basic_widgets(self):

        """
        Subframe structure

        [0][0][5][5]
        [1][2][6][6]
        [3][3][6][6]
        [4][4][6][6]

        Where:
            [0] : Subtitle of the size input widget
            [1] : Size input widget
            [2] : Size input button
            [3] : Subtitle of the table input widget
            [4] : Table input widget (null-space before set the size)
            [5] : Subtitle of the output widget
            [6] : Output printer
        """

        w_half = self.get_subframe(0.5)[0]
        w_tenth = self.get_subframe(0.1)[0]

        # [0]
        self.size_label = tk.Label(self, text="Size of Sudoku:", width=w_half)
        self.size_label.grid(row=0, column=0, columnspan=2)

        # [1]
        self.size_entry = tk.Entry(self, width=w_tenth)
        self.size_entry.grid(row=1, column=0, sticky='en')

        # [2]
        self.get_table_button = tk.Button(self, text="Set Sudoku Table", command=self.create_table_widgets)
        self.get_table_button.grid(row=1, column=1, sticky='wn')

        # [3]
        self.mat_label = tk.Label(self, text="Table of Sudoku:", width=w_half)
        self.mat_label.grid(row=2, column=0, columnspan=2)

        # [4]
        self.mat_null = tk.Text(self, width=w_half, bg='#E0E0E0')
        self.mat_null.grid(row=3, column=0, columnspan=2)

        # [5]
        self.result_label = tk.Label(self, text="Result:", width=w_half)
        self.result_label.grid(row=0, column=2, columnspan=2)

        # [6]
        self.result_text = tk.Text(self, width=w_half)
        self.result_text.grid(row=1, column=2, rowspan=3, columnspan=2)
        return
    
    def create_table_widgets(self):
        size_str = self.size_entry.get()
        if not size_str.isdigit():
            print('Error')
        elif int(size_str) not in [2, 3, 4]:
            print('Another Error')
        else:
            self.size = int(size_str)
            self.size2 = self.size ** 2
            self.relocate_widgets()

            # Create solve button
            self.solve_button = tk.Button(self, text="Solve", command=self.create_result_widgets)
            self.solve_button.grid(row=self.size2 + 3, column=0, columnspan=self.size2)
        return
    
    def relocate_widgets(self):
        # Adjust existing widget layout
        self.size_label.grid(row=0, column=0, columnspan=self.size2)
        self.size_entry.grid(row=1, column=0, columnspan=self.size2 // 2, sticky='en')
        self.get_table_button.grid(row=1, column=self.size2 // 2, columnspan=self.size2 // 2, sticky='wn')
        self.mat_label.grid(row=2, column=0, columnspan=self.size2)
        self.result_label.grid(row=0, column=self.size2)
        self.result_text.grid(row=1, column=self.size2, rowspan=self.size2 + 3)

        # Create matrix entry
        self.mat_null.destroy()
        w_elem = self.get_subframe(0.5 / self.size2)[0]
        self.mat_entry_list = []
        for row in range(self.size2):
            for col in range(self.size2):
                mat_entry = tk.Entry(self, width=w_elem)
                mat_entry.bind('<Tab>')
                mat_entry.bind('<Shift-Tab>')
                mat_entry.grid(row=row + 3, column=col)
                self.mat_entry_list.append(mat_entry)
        return
    
    def create_result_widgets(self):
        data = self.get_data()

        start = datetime.now()
        try:
            solver = SquareSudokuSolver(data, self.size)
            solver.solve()
            validity = True
        except ValueError:
            print('ValueError')
            validity = False
        except Exception as e:
            validity = False
            print(e)
        end = datetime.now()

        string_out = '-' * 28
        string_out += '\nResult:'
        string_out += '\n{}'.format(solver.mat_obj if validity else None)
        string_out += '\nStatistic:'
        string_out += '\n    total time : {:>8.3f} ms'.format((end - start).microseconds / 1000)
        string_out += '\n    validity   : {!s:>11}'.format(validity)
        string_out += '\n' + '-' * 28
        self.result_text.delete('1.0', 'end')
        self.result_text.insert(tk.END, string_out)
        return
    
    def get_data(self):
        data = [[None] * self.size2 for _ in range(self.size2)]
        for i, elem in enumerate(self.mat_entry_list):
            digit_str = elem.get()
            if digit_str == '':
                digit = None
            elif digit_str.isdigit():
                digit = int(digit_str)
            else:
                print('Error')
                break
            data[i // self.size2][i % self.size2] = digit
        return data


if __name__ == '__main__':
    configs = {'master_title': 'Squared Sudoku Solver',
            #    'icon': './figure/sudoku_icon.ico',
               'window_size': (1000, 400),
               'resizable': False}
    
    try:
        root = tk.Tk()
        app = SudokuAppWindow(root, **configs)
        app.mainloop()
    except Exception as e:
        print(f'Exception occured: {e}')

# from tkinter import *

# root = Tk()

# t1 = Text(root)
# t1.pack(side=TOP)

# t2 = Text(root)
# t2.pack(side=TOP)

# def focusNext(widget):
#     widget.tk_focusNext().focus_set()
#     return 'break'

# def focusPrev(widget):
#     widget.tk_focusPrev().focus_set()
#     return 'break'

# for t in (t1, t2):
#     t.bind('<Tab>', lambda e, t=t: focusNext(t))
#     t.bind('<Shift-Tab>', lambda e, t=t: focusPrev(t))

# t1.focus_set()

# root.mainloop()
