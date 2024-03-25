# Connect.py 
# Name: Mikaela Teowratanakul & Joseph Rainford
# email: teowramm@mail.uc.edu & rainfojp@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: March 28, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment tests our teamwork skills, by having two people work on one single project. This can be accomplished with GitHub and utilizing different packages.

# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this: This module calls a SQL query to the database created by Professor Nicholson, refines some of the results and stores them in a list.
# Citations: NA
# Anything else that's relevant: NA
    
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                      'Database=IS4010;'
                      'uid=IS4010Login;'
                      'pwd=P@ssword2;')


cursor = conn.cursor()

cursor.execute('''
                SELECT 
                    [GroceryStoreSimulator].[dbo].[tStore].[StoreID], 
                    [GroceryStoreSimulator].[dbo].[tStoreStatus].[StoreStatus], 
                    COUNT([GroceryStoreSimulator].[dbo].[tLoyalty].[LoyaltyID]) AS NmLoyal 
                FROM 
                    [GroceryStoreSimulator].[dbo].[tStoreHistory] 
                    INNER JOIN [GroceryStoreSimulator].[dbo].[tStore] 
                        ON [GroceryStoreSimulator].[dbo].[tStore].[StoreID] = [GroceryStoreSimulator].[dbo].[tStoreHistory].[StoreID] 
                    INNER JOIN [GroceryStoreSimulator].[dbo].[tStoreStatus] 
                        ON [GroceryStoreSimulator].[dbo].[tStoreHistory].[StoreStatusID] = [GroceryStoreSimulator].[dbo].[tStoreStatus].[StoreStatusID] 
                    INNER JOIN [GroceryStoreSimulator].[dbo].[tLoyalty] 
                        ON [GroceryStoreSimulator].[dbo].[tStoreHistory].[StoreID] = [GroceryStoreSimulator].[dbo].[tLoyalty].[StoreID] 
                    WHERE 
                        [GroceryStoreSimulator].[dbo].[tStore].[State] = 'OH' 
                    GROUP BY 
                        [GroceryStoreSimulator].[dbo].[tStore].[StoreID],
                        [GroceryStoreSimulator].[dbo].[tStoreStatus].[StoreStatus]
                    ORDER BY 
                        [GroceryStoreSimulator].[dbo].[tStore].[StoreID]
                ''')



    
storestatusList = list()



for row in cursor:
    if row.StoreStatus.strip() == "On Fire":
        storestatusList.append((row.StoreID, row.NmLoyal))

if __name__ == "__main__":
    print(storestatusList) # number of loyalty customers that the store with storeID =2 lost when they closed due to the fire






