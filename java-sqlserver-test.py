import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'localhost' 
database = 'PyLearnDB' 
username = 'sa' 
password = '***' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';TrustServerCertificate=yes;ENCRYPT=no;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO Test (Name) VALUES (?);"
with cursor.execute(tsql,'Mehdi'):
    print ('Successfully Inserted!')


#Update Query
print ('Updating Location for Mehdi')
tsql = "UPDATE Test SET Name = ? WHERE Name = ?"
with cursor.execute(tsql,'Mehdi Amiri','Mehdi'):
    print ('Successfully Updated!')


#Delete Query
print ('Deleting user Jared')
tsql = "DELETE FROM Test WHERE Name = ?"
with cursor.execute(tsql,'Mehdi Amiri'):
    print ('Successfully Deleted!')

print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO Test (Name) VALUES (?);"
with cursor.execute(tsql,'Mehdi'):
    print ('Successfully Inserted!')

#Select Query
print ('Reading data from table')
tsql = "SELECT Name FROM Test;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]))
        row = cursor.fetchone()
