
    
import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')

cursor = conn.cursor()

cursor.execute('SELECT [GroceryStoreSimulator].[dbo].[tStore].[StoreID], [GroceryStoreSimulator].[dbo].[tStoreStatus].[StoreStatus], COUNT([GroceryStoreSimulator].[dbo].[tLoyalty].[LoyaltyID]) AS NmLoyal FROM [GroceryStoreSimulator].[dbo].[tStoreHistory] INNER JOIN [GroceryStoreSimulator].[dbo].[tStore] ON [GroceryStoreSimulator].[dbo].[tStore].[StoreID] = [GroceryStoreSimulator].[dbo].[tStoreHistory].[StoreID] INNER JOIN [GroceryStoreSimulator].[dbo].[tStoreStatus] ON [GroceryStoreSimulator].[dbo].[tStoreHistory].[StoreStatusID] = [GroceryStoreSimulator].[dbo].[tStoreStatus].[StoreStatusID] INNER JOIN [GroceryStoreSimulator].[dbo].[tLoyalty] ON [GroceryStoreSimulator].[dbo].[tStoreHistory].[StoreID] = [GroceryStoreSimulator].[dbo].[tLoyalty].[StoreID] GROUP BY [GroceryStoreSimulator].[dbo].[tStore].[StoreID], [GroceryStoreSimulator].[dbo].[tStoreStatus].[StoreStatus] ORDER BY [GroceryStoreSimulator].[dbo].[tStore].[StoreID]') # edit this to put code inside parentheses (SELECT, FROM, WHERE)



    
storestatusList = list()



for row in cursor:
    if row.StoreStatus == "On Fire                                                                                             " and row.StoreID ==2:
        storestatusList.append((row.NmLoyal))
print(storestatusList) # number of loyalty customers that the store with storeID =2 lost when they closed due to the fire






