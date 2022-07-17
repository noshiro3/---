from asyncio.windows_events import NULL
from platform import java_ver
import sqlite3
from unicodedata import name

#新しいDBを作り接続する。既存なら再接続
dbname = 'EC_table'
conn = sqlite3.connect(dbname)

#カーソルの作成
c = conn.cursor()

# c.execute('CREATE TABLE Reason_return (商品名 VARCHAR(20) PRIMARY KEY,サイズが合わない int,必要なくなった int,似合わなかった int,画像と違った int,破損があった int,その他 int)')
# c.execute('INSERT INTO Reason_return VALUES("白いTシャツ",25,40,10,5,15,0)')
# conn.commit()


class Reason_for_return():

    #返品理由を選択する
    change_value_message = ""

    def reason_for_return(self):

        #table名はReason_returen
        c.execute('SELECT * FROM Reason_return')
        Reason_return_item = c.fetchone()
        
        print('返品理由->')
        check_Reason_return = input()
        if check_Reason_return == 'サイズが合わない':
            c.execute(f'UPDATE Reason_return set サイズが合わない = {Reason_return_item[1]+1}')
            change_value_message = "「サイズが合わない」に一人追加しました"
        elif check_Reason_return == '必要なくなった':
            c.execute(f'UPDATE Reason_return set 必要なくなった = {Reason_return_item[2]+1}')
            change_value_message = "「必要なくなった」に一人追加しました"
        elif check_Reason_return == '似合わなかった':
            c.execute(f'UPDATE Reason_return set 似合わなかった = {Reason_return_item[3]+1}')        
            change_value_message = "「似合わなかった」に一人追加しました"
        elif check_Reason_return == '画像と違った':
            c.execute(f'UPDATE Reason_return set 画像と違った = {Reason_return_item[4]+1}')
            change_value_message = "「画像と違った」に一人追加しました"
        elif check_Reason_return == '破損があった':
            c.execute(f'UPDATE Reason_return set 破損があった = {Reason_return_item[5]+1}')
            change_value_message = "「破損があった」に一人追加しました"
        elif check_Reason_return == 'その他':
            c.execute(f'UPDATE Reason_return set その他 = {Reason_return_item[6]+1}')
            change_value_message = "「その他」に一人追加しました"

        #返品数の合計
        Reason_return_item_sum = Reason_return_item[1]+Reason_return_item[2]+Reason_return_item[3]+Reason_return_item[4]+Reason_return_item[5]+Reason_return_item[6]
        # comprehensivec_review_sum = c.execute('SELECT 返品数 FROM Comprehensive')
        # if Reason_return_item_sum == comprehensivec_review_sum:
        #     conn.commit()        


#カーソルとデータベースの接続を閉じる    
c.close()
conn.close()

#消したくないけど使わないやつをおいておくところ
class unUse():
    name = ""
#返品理由のテーブルを作成(最初だけ)
#c.execute('CREATE TABLE Reason_return (商品名 VARCHAR(20) PRYMARY KEY,サイズが合わない int,必要なくなった int,似合わなかった int,画像と違った int,破損があった int,その他 int)')

#仮データを初期値として入力(最初だけ)
# c.execute('INSERT INTO Reason_return VALUES("白いTシャツ",25,40,10,5,15,0)')

#データを消したいときに使う
# c.execute('DELETE FROM Reason_return where サイズが合わない = 41')