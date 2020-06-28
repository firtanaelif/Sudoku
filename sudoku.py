from csp import *
from datetime import datetime

with open("sudoku3.txt", "r") as file:
    a = file.read().split("\n")
sudoku_inputs = ""

for i in range(9):
    row = a[i].split(",")
    for x in row:
        sudoku_inputs += x

sudoku_inputs = sudoku_inputs.replace("0",".")
sudoku = Sudoku(sudoku_inputs)
sudoku.display(sudoku.infer_assignment())

print("\n## Solved with backtracking only ##\n")
before = datetime.now()
search = backtracking_search(sudoku)
after = datetime.now()
sudoku.display(sudoku.infer_assignment())
print("Running Time -->", (after - before).total_seconds())

print("\n## Solved with backtracking + mrv + lcv + ac3 ##\n")
before = datetime.now()
search = backtracking_search(sudoku, select_unassigned_variable=mrv, order_domain_values=lcv, inference=mac)
after = datetime.now()
sudoku.display(sudoku.infer_assignment())
print("Running Time -->", (after - before).total_seconds())

