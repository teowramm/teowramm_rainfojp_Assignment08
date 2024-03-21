


import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()

cursor.execute('SELECT') # edit this to put code inside parentheses (SELECT, FROM, WHERE)

loyaltyList = list()

for row in cursor:
    if row.Loyalty ==3 # edit this
    loyaltyList.append(row.Loyalty.rstrip(" "))
print(loyaltyList)