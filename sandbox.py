from asyncio.windows_events import NULL
from select import select
import sqlite3
from zlib import compressobj

#新しいDBを作り接続する。既存なら再接続
dbname = 'EC_table'
conn = sqlite3.connect(dbname)

c = conn.cursor()


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

value = calculator()
print("選んだ商品の信頼度は" + str(100 + value) + "点/100点です。")

c.close()
conn.close()


