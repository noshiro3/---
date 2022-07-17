#データベースの値の変更をするファイル
import sqlite3 

dbname = 'EC_table'
conn = sqlite3.connect(dbname)

c = conn.cursor()

#返品するメソッド
def reason_for_return():

    change_value_message = ""
    change_Reason_return = False

    #table名はReason_returen
    c.execute('SELECT * FROM Reason_return')
    Reason_return_item = c.fetchone()
    
    print('返品理由->')
    check_Reason_return = input()
    if check_Reason_return == 'サイズが合わない':
        c.execute(f'UPDATE Reason_return set サイズが合わない = {Reason_return_item[1]+1}')
        change_value_message = "「サイズが合わない」に一人追加しました"
        change_Reason_return = True
    elif check_Reason_return == '必要なくなった':
        c.execute(f'UPDATE Reason_return set 必要なくなった = {Reason_return_item[2]+1}')
        change_value_message = "「必要なくなった」に一人追加しました"
        change_Reason_return = True
    elif check_Reason_return == '似合わなかった':
        c.execute(f'UPDATE Reason_return set 似合わなかった = {Reason_return_item[3]+1}')        
        change_value_message = "「似合わなかった」に一人追加しました"
        change_Reason_return = True
    elif check_Reason_return == '画像と違った':
        c.execute(f'UPDATE Reason_return set 画像と違った = {Reason_return_item[4]+1}')
        change_value_message = "「画像と違った」に一人追加しました"
        change_Reason_return = True
    elif check_Reason_return == '破損があった':
        c.execute(f'UPDATE Reason_return set 破損があった = {Reason_return_item[5]+1}')
        change_value_message = "「破損があった」に一人追加しました"
        change_Reason_return = True
    elif check_Reason_return == 'その他':
        c.execute(f'UPDATE Reason_return set その他 = {Reason_return_item[6]+1}')
        change_value_message = "「その他」に一人追加しました"
        change_Reason_return = True
    
    if change_Reason_return == True:
        print(change_value_message)
        c.execute('SELECT 返品数 FROM Comprehensive')
        Comprehensive_item = c.fetchone()
        #返品数を+1する
        c.execute(f'UPDATE Comprehensive set 返品数 = {Comprehensive_item[0]+1}') 
        # conn.commit()

#Reason_returnテーブルを確認
def show_Reason_return_table():
    c.execute('SELECT * FROM Reason_return')
    for row in c:
        print(row)

#Comprehensiveテーブルを確認
def show_Comprehensive_table():
    c.execute('SELECT * FROM Comprehensive')
    for row in c:
        print(row)

reason_for_return()
show_Reason_return_table()
show_Comprehensive_table()

c.close()
conn.close()


#仮データを初期値として入力(最初だけ)
# c.execute('INSERT INTO Reason_return VALUES("白いTシャツ",25,40,10,5,15,0)')
# c.execute('INSERT INTO Comprehensive VALUES("白いTシャツ",1000,95,739,32,37,74,152,444)')