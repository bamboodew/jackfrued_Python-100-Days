import xlrd

from datetime import date, datetime

file = 'test3.xls'


def read_excel():
    # 打开文件;读取文件的时候需要将formatting_info参数设置为True，默认是False
    wb = xlrd.open_workbook(filename=file, formatting_info=True)
    # 获取所有表格名字
    print(wb.sheet_names())

    # 通过索引获取表格
    sheet1 = wb.sheet_by_index(0)
    # 通过名字获取表格
    sheet2 = wb.sheet_by_name('年级')

    print(sheet1, sheet2)
    print(sheet1.name, sheet1.nrows, sheet1.ncols)

    # 获取行内容
    rows = sheet1.row_values(2)
    # 获取列内容
    cols = sheet1.col_values(3)
    print(rows)
    print(cols)

    # 获取表格里的内容，三种方式
    print(sheet1.cell(1, 0).value)
    print(sheet1.cell_value(1, 0))
    print(sheet1.row(1)[0].value)

    print(sheet1.cell(1, 2).ctype)
    date_value = xlrd.xldate_as_tuple(sheet1.cell_value(1, 2), wb.datemode)
    print(date_value)
    print(date(*date_value[:3]))
    print(date(*date_value[:3]).strftime('%Y/%m/%d'))

    print(sheet1.merged_cells)
    print(sheet1.cell_value(1, 3))
    print(sheet1.cell_value(4, 3))
    print(sheet1.cell_value(6, 1))


if __name__ == '__main__':
    read_excel()
