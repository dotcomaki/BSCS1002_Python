'''
Chess Question
'''

start = input()
end = input()

cols = 'ABCDEFGH'
rows = '12345678'

start_col, start_row = start[0], start[1]
end_col, end_row = end[0], end[1]

col_diff = cols.index(start_col) - cols.index(end_col)
row_diff = rows.index(start_row) - rows.index(end_row)

if abs(col_diff) == abs(row_diff):
    print('YES')
else:
    print('NO')
