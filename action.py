#データベースの値の変更をするファイル
from select import select
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
    
    print('返品理由->',end='')
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
    conn.commit()

#計算するメソッド
def calculator():

    #返品理由の計算メソッド
    def reason_for_return_calculator():
        c.execute(f'SELECT * FROM Reason_return WHERE 商品名 = "{select_product}"')
        Reason_return_item = c.fetchone()
        
        #初期化
        Reason_return_item_sum = 0
        #返品理由の数を計算する
        for i in range(1,6):
            Reason_return_item_sum = Reason_return_item_sum + Reason_return_item[i]
        #返品理由の内訳
        Reason_return_item_sum2 = [0,0,0,0,0,0] #配列
        Reason_return_item_sum2[0] = Reason_return_item[1]*-6
        Reason_return_item_sum2[1] = Reason_return_item[2]*-6
        Reason_return_item_sum2[2] = Reason_return_item[3]*0
        Reason_return_item_sum2[3] = Reason_return_item[4]*-24
        Reason_return_item_sum2[4] = Reason_return_item[5]*-30
        Reason_return_item_sum2[5] = Reason_return_item[6]*0
        #掛け算したあとの合計

        #初期化
        total_Reason_return_item_sum2 = 0
        #掛け算後の点数を合計する
        for i in range(0,5):
            total_Reason_return_item_sum2 = total_Reason_return_item_sum2 + Reason_return_item_sum2[i]
        #最終得点
        total_score = total_Reason_return_item_sum2/Reason_return_item_sum

        return round(total_score)

    # return reason_for_return_calculator()
    

    #返品率を計算
    def return_rate():
        c.execute(f'SELECT * FROM Comprehensive WHERE 商品名 = "{select_product}"')
        Comprehensive_item = c.fetchone()
        #(返品数/販売数)*100
        total_score = (Comprehensive_item[2]/Comprehensive_item[1])*100
        if total_score > 60:
            total_score =  -20
        elif total_score > 45:
            total_score = -15
        elif total_score > 30:
            total_score = -10
        elif total_score > 15:
            total_score = -5
        else:
            total_score = 0
        
        return total_score
    
    def review_rate():
        c.execute(f'SELECT 星1,星2,星3,星4,星5 FROM Comprehensive WHERE 商品名 = "{select_product}"')
        Comprehensive_item = c.fetchone()
        #レビューの数の合計
        Comprehensive_item_total = 0
        for i in range(0,4):
            Comprehensive_item_total = Comprehensive_item_total + Comprehensive_item[i]
        #レビューの点数の合計
        Comprehensive_item_sum = Comprehensive_item[0]+Comprehensive_item[1]*2+Comprehensive_item[2]*3+Comprehensive_item[3]*4+Comprehensive_item[4]*5
        total_score = 0
        #平均評価点を算出
        Comprehensive_item_ave = round(Comprehensive_item_sum/Comprehensive_item_total,1)
        if Comprehensive_item_ave > 4:
            total_score = 0
        elif Comprehensive_item_ave > 3:
            total_score = -5
        elif Comprehensive_item_ave > 2:
            total_score = -10
        elif Comprehensive_item_ave > 1:
            total_score = -15
        else:
            total_score = -20

        return total_score

    def purchase_value():
        c.execute(f'SELECT * FROM Customer_purchase WHERE 商品名 = "{select_product}"')
        Customer_purchase_item = c.fetchone()
        #total_scoreを出すための点数
        Customer_purchase_item_sum = Customer_purchase_item[1]*0+Customer_purchase_item[2]*-15+Customer_purchase_item[3]*-20
        #購入数の総数
        Customer_purchase_item_total = Customer_purchase_item[1]+Customer_purchase_item[2]+Customer_purchase_item[3]

        total_score = Customer_purchase_item_sum/Customer_purchase_item_total
        return round(total_score)

    #共通する動作
    print('商品名を入力してください->', end='')
    select_product = input()
    return return_rate()+reason_for_return_calculator()+review_rate()+purchase_value()

print('返品なら「1」点数を確認するなら「2」->',end='')
select_action = int(input())
if select_action == 1:
    reason_for_return()
elif select_action == 2:
    value = calculator()
    print("選んだ商品の信頼度は" + str(100 + value) + "点/100点です。")

c.close()
conn.close()


#仮データを初期値として入力(最初だけ)
# c.execute('INSERT INTO Reason_return VALUES("白いTシャツ",25,40,10,5,15,0)')
# c.execute('INSERT INTO Comprehensive VALUES("白いTシャツ",1000,95,739,32,37,74,152,444)')
# c.execute('INSERT INTO Customer_purchase VALUES("白いTシャツ",980,20,0)')

#黒いTシャツを追加(すでにした)
# c.execute('INSERT INTO Reason_return VALUES("黒いTシャツ",500,600,200,500,1000,0)')
# c.execute('INSERT INTO Comprehensive VALUES("黒いTシャツ",5000,2800,315,60,125,60,30,40)')
# c.execute('INSERT INTO Customer_purchase VALUES("黒いTシャツ",2000,1500,1500)')

#Reason_returnテーブルを作成(最初だけ)
#c.execute('CREATE TABLE Reason_return (商品名 VARCHAR(20) PRIMARY KEY,サイズが合わない int,必要なくなった int,似合わなかった int,画像と違った int,破損があった int,その他 int)')

#Comprehensiveテーブルを作成(最初だけ)
# c.execute('CREATE TABLE Comprehensive (商品名 VARCHAR(20) PRIMARY KEY,販売数 int DEFAULT 0,返品数 int DEFAULT 0,評価数 int DEFAULT 0,星1 int DEFAULT 0,星2 int DEFAULT 0,星3 int DEFAULT 0,星4 int DEFAULT 0,星5 int DEFAULT 0)')

#customer_purchaseテーブルの作成
# c.execute('CREATE TABLE Customer_purchase (商品名 VARCHAR(20) PRIMARY KEY,U_4 int DEFAULT 0,B5AND10 int DEFAULT 0,O_11 int DEFAULT 0)')

