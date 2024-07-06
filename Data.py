import openpyxl

path = "./DataHolder.xlsx"
row=int
column=int

wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active

cell_obj = sheet_obj.cell(row=1, column=1)

print(cell_obj.value)

row = input("Enter your row: ")
column = input("Enter your your columns: ")
row = int(row)
column = int(column)

print("Total Rows:", row) 
print("Total Columns:", column) 
  
print("\nValue of first column") 
for i in range(1, row + 1): 
    cell_obj = sheet_obj.cell(row=i, column=1) 
    print(i, cell_obj.value) 
  
print("\nValue of first row") 
for i in range(1, column + 1): 
    cell_obj = sheet_obj.cell(row, column=i) 
    print(cell_obj.value, end=" ") 