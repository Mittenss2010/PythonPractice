import xlrd
import os

file = 'test.xlsx'

def read_excel():

    wb = xlrd.open_workbook(filename=file)        #打开文件
    print(wb.sheet_names())                       #获取所有表格名字

    sheet1 = wb.sheet_by_index(0)                 #通过索引获取表格
    sheet2 = wb.sheet_by_name('项目属性分析')     #通过名字获取表格
    print(sheet1,sheet2)
    
    print(sheet2.name,sheet2.nrows,sheet1.ncols)

    #rows = sheet1.row_values(2)                   #获取行内容
    cols = sheet2.col_values(0)                    #获取sheet2 的 列内容
    #print(rows)
    # print(cols)
    
    count=0
    print(len(cols))
    for item in cols:
        newFileName = item.split(' ')
        if len(newFileName)>1:
            print(newFileName[1])
            count+=1
            os.makedirs(str(count) + newFileName[1])

    print(count)

    #print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
    #print(sheet1.cell_value(1,0))
    #print(sheet1.row(1)[0].value)

    
read_excel()