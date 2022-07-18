#データベースの中身を確認
import sqlite3 

dbname = 'EC_table'
conn = sqlite3.connect(dbname)

c = conn.cursor()

print('Reason_returnテーブル')
c.execute('SELECT * FROM Reason_return')
for row in c:
    print(row)
print('Comprehensiveテーブル')
c.execute('SELECT * FROM Comprehensive')
for row in c:
    print(row)
print('Customer_purchaseテーブル')
c.execute('SELECT * FROM Customer_purchase')
for row in c:
    print(row)

c.close()
conn.close()
