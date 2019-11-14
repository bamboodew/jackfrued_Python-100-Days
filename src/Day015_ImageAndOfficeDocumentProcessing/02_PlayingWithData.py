from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws1 = wb.create_sheet('MySheet')  # insert at the end (default)
ws2 = wb.create_sheet('MySheet1', 0)  # insert at first position
ws3 = wb.create_sheet('MySheet2', -1)  # insert at the penultimate position
ws.title = 'New Title'
ws.sheet_properties.tabColor = '1072BA'
ws3 = wb['New Title']
# print(wb.sheetnames)
# for sheet in wb:
#     print(sheet.title)
source = wb.active
target = wb.copy_worksheet(source)
"""
Accessing one cell
Now we know how to get a worksheet,
we can start modifying cells content.
Cells can be accessed directly as keys of the worksheet:
"""
ws['A4'] = 4
c = ws['A4']
# c.value = 'hello, world'
d = ws.cell(row=4, column=2, value=10)
# print(c)
# print(c.value)

# print(d)
# print(d.value)

for x in range(1, 101):
    for y in range(1, 101):
        ws.cell(row=x, column=y)

cell_range = ws['A1':'C2']  # 切片
# print(cell_range)  # 二维元组：先行再列
colC = ws['C']  # 共计1列、100行
# print(colC)  # 一维元组
col_range = ws['C:D']  # 共计2列、100行
# print(col_range)  # 先列再行
row10 = ws[10]
# print(row10)
row_range = ws[5:10]  # 先行再列
# print(row_range)

'''先行后列'''
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    for cell in row:
        print(cell)

print()
'''先列后行'''
for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
    for cell in col:
        print(cell)
print()
print(tuple(ws.rows))
print(tuple(ws.columns))
