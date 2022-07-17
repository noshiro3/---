import sqlite3

dbname = 'simple_calculation'
conn = sqlite3.connect(dbname)

#カーソル作成
c = conn.cursor()

#なんか消すやつ
c.execute('DELETE FROM sample')

conn.commit()

c.close()
conn.close()