import datetime

from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.utils import FORMULAE

wb = Workbook()
ws = wb.active
ws['A1'] = datetime.datetime(2010, 7, 21)
print(ws['A1'].number_format)

ws["A2"] = "=SUM(1,1)"

print('HEX2DEC' in FORMULAE)

ws.merge_cells('A3:D3')
# ws.unmerge_cells('A3:D3')
ws.merge_cells(start_row=4, start_column=1, end_row=5, end_column=5)
# ws.unmerge_cells(start_row=4, start_column=1, end_row=5, end_column=5)

# Inserting an image
ws['A6'] = 'You should see logo below'
img = Image('logo.png')
ws.add_image(img, 'A7')

wb.save('formula.xlsx')
