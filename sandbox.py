import sqlite3

#新しいDBを作り接続する。既存なら再接続
dbname = 'EC_table'
conn = sqlite3.connect(dbname)

c = conn.cursor()


def calculator():

    #返品理由の計算メソッド
    def reason_for_return_calculator():
        c.execute('SELECT * FROM Reason_return')
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

    return reason_for_return_calculator()

print(calculator())

c.close()
conn.close()


