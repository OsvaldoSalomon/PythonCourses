import openpyxl
from openpyxl.styles import *

print(dir(openpyxl.styles))

workbook = openpyxl.load_workbook("E:/osvaldo/PythonExercises/03ThirdCourse/Excel/Employees.xlsx")

sheet = workbook['Skills']
cell = sheet['B8']

font = Font(color='CC33FF', bold=True, italic=True)

cell.font = font

fill = PatternFill(fill_type='solid', bgColor='F7FE2E')

cell.fill = fill

border = Border(left=Side(border_style='double', color='322FEC'), right=Side(border_style='double', color='322FEC'),
                top=Side(border_style='double', color='322FEC'), bottom=Side(border_style='double', color='322FEC'))

cell.border = border

alignment = Alignment(horizontal='left')

cell.alignment = alignment

workbook.save("E:/osvaldo/PythonExercises/03ThirdCourse/Excel/Employees.xlsx")

