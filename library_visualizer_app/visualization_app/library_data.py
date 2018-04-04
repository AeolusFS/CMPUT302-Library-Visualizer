# This library will import all the data from xlsx file and store
# in python dictionary with the format below

# lib_info format
#    ' ':{
#        'Name':'',
#        'Git_Rep': ,
#        'Domain': ,
#        'Popularity_Count': ,
#        'Last_Modification_Date':
#        'Last_Discussed_SO':' ',
#        '#_Questions_Asked_SO': ,
#        'Release_Dates':[],
#        '#_Breaking_Changes':[],
#        'issue_data':{
#            1:{
#               'Issue_Creation_Date':' ',
#               'Issue_Close_Date':' ',
#               'Date_of_First_Comment': ,
#               'Performance_Issue': ,
#               'Security_Issue':
#            }
#            ...
#        }
#    }

# Sample access example
# EX. junit4 github repository
# lib_info[junit4][Git_Rep] = junit-team/junit4
# lib_info[junit4][issue_data][1][Performance_Issue] = False

import xlrd

def remove_values_from_list(the_list, value):
    while value in the_list:
        the_list.remove(value)

# Read xlsx and initialize datemode
data = xlrd.open_workbook(r"C:\Users\Zakia\Desktop\302Project\library_visualizer_app\visualization_app\Metric_Data.xlsx")
lib_info = {}

data_datemode = data.datemode


# Read chart Library Info
table = data.sheet_by_name('Library Info')
nrows = table.nrows
lib_name = []

for i in range(1,nrows):
    row_value = table.row_values(i)
    lib_name.append(row_value[0])
    new_lib = {row_value[0]:{}}
    lib_info.update(new_lib)
    lib_update = {
        'Name':row_value[0],
        'Git_Rep':row_value[1],
        'Domain':row_value[2]
    }
    lib_info[row_value[0]].update(lib_update)



# Read chart Popularity
table = data.sheet_by_name('Popularity')
nrows = table.nrows

for i in range(1,nrows):
    row_value = table.row_values(i)
    lib_update = {
        'Popularity_Count':row_value[1]
    }
    lib_info[row_value[0]].update(lib_update)




# Read chart Release Frequency
table = data.sheet_by_name('Release Frequency')
ncols = table.ncols
lib_num = 0

for i in range(0,ncols):
    col_value = table.col_values(i)
    col_value.pop(0)
    remove_values_from_list(col_value,'')
    date_value = []
    for value in col_value:
        y, m, d, h, mi, s = xlrd.xldate_as_tuple(value, data_datemode)
        date_value.append("{0}-{1}-{2}".format(y, m, d))
    lib_update = {
        'Release_Dates':date_value
    }
    lib_info[lib_name[lib_num]].update(lib_update)
    lib_num += 1




# Read chart Last Modification Date
table = data.sheet_by_name('Last Modification Date')
nrows = table.nrows

for i in range(1,nrows):
    row_value = table.row_values(i)
    y, m, d, h, mi, s = xlrd.xldate_as_tuple(row_value[1], data_datemode)
    lib_update = {
        'Last_Modification_Date':("{0}-{1}-{2}".format(y, m, d))
    }
    lib_info[row_value[0]].update(lib_update)





# Read chart Backwards Compatibility
table = data.sheet_by_name('Backwards Compatibility')
ncols = table.ncols
lib_num = 0

for i in range(1,ncols):
    col_value = table.col_values(i)
    col_value.pop(0)
    remove_values_from_list(col_value,'')
    lib_update = {
        '#_Breaking_Changes':col_value
    }
    lib_info[lib_name[lib_num]].update(lib_update)
    lib_num += 1






# Read chart Last Discussed on Stack Overflow
table = data.sheet_by_name('Last Discussed on Stack Overflo')
nrows = table.nrows

for i in range(1,nrows):
    row_value = table.row_values(i)
    date_value = 'Never'
    if row_value[1] != 'Never':
        y, m, d, h, mi, s = xlrd.xldate_as_tuple(row_value[1], data_datemode)
        date_value = ("{0}-{1}-{2}".format(y, m, d))
    lib_update = {
        'Last_Discussed_SO':date_value,
        '#_Questions_Asked_SO':row_value[2]
    }
    lib_info[row_value[0]].update(lib_update)





# Read chart Issue Data
table = data.sheet_by_name('Issue Data')
nrows = table.nrows

for i in range(0,nrows):
    STATUS = 'NOT FOUND'

print (lib_info)
