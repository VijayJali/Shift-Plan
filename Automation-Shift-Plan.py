Ranges of cells can be accessed using slicing

>>> cell_range = ws['A1':'C2']
Ranges of rows or columns can be obtained similarly:

>>> colC = ws['C']
>>> col_range = ws['C:D']
>>> row10 = ws[10]
>>> row_range = ws[5:10]
