from asyncio.windows_events import NULL
import sqlite3

#新しいDBを作り接続する。
dbname = 'simple_calculation'
conn = sqlite3.connect(dbname)

c = conn.cursor()

#入力を受け付ける
print('なんか入力してね')
new_sql = input()
if new_sql != NULL:
    c.execute(f'INSERT INTO sample(id) values({new_sql})')

# c.execute('CREATE TABLE sample (id int)')
# c.execute('INSERT INTO sample(id) values(9999)')

#入力した値をSQLに保存
conn.commit()

c.execute('SELECT id FROM sample')

for row in c:
    print(row)

#カーソル閉じる
c.close()
#データベースを終了する時は絶対に閉じる。
conn.close()