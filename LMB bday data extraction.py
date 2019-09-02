import xlrd
import xlwt

wb = xlrd.open_workbook('lmb updated list.xlsx')
sheet = wb.sheet_by_index(0)

months = ['jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec']
info =[]
book = xlwt.Workbook()
for month in months:
    month_info =[]
    for i in range(sheet.nrows):
        if i != 0:
            if month in sheet.cell_value(i,8).lower():
                details = []
                details.append(sheet.cell_value(i,0))
                details.append(sheet.cell_value(i,1))
                details.append(sheet.cell_value(i,8))
                month_info.append(details)
    sheet1 = book.add_sheet(month)
    for j in range(3):
        for i in range(len(month_info)):       
            sheet1.write(i,j,month_info[i][j])
    month_name = month + '.xls'
book.save('LMB birthday list.xls')
