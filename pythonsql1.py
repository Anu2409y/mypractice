import pyodbc
import pandas as pd

# Replace with your actual server and DB info
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=YALAVARTHI;'
    'DATABASE=db1;'
    'UID=sa;'
    'PWD=Sranyc@2420;'
)

#cursor = conn.cursor()

# Example query
'''cursor.execute("SELECT TOP 10 * FROM Employee")

for row in cursor.fetchall():
    print(row)'''

df = pd.read_sql("SELECT * FROM Employee", conn)
print(df.head())
df.to_csv('transfer.csv', index=False)


#cursor.close()
conn.close()



