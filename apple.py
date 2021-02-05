sells={'num':0,
       'price':0,
       'sell':0}
persells=[]

while True:
    print('功能==>')
    print('1.設定')
    print('2.進貨')
    print('3.出貨')
    print('4.營業額統計')
    print('5.庫存')
    print('6.離開系統')

    sel = input('請輸入欲執行選項:')

    if sel=='1': # 設定
        sells['num']=int(input('設定蘋果數量:'))
        sells['price']=int(input('一顆單價:'))
        print('蘋果目前有', sells['num'], '顆')
        print('蘋果一顆', sells['price'], '元')
    elif sel=='2': # 進貨
        numin = int(input('進了多少顆蘋果?'))
        sells['num'] = sells['num'] + numin
        print('蘋果目前有', sells['num'], '顆')
    elif sel=='3': # 出貨
        numout = int(input('輸入出貨數量:'))
        print('應付', numout*sells['price'], '元')
        sells['num'] = sells['num'] - numout
        sells['sell'] = sells['sell'] + numout
        temp_sells=[]
        temp_sells.append(numout)
        temp_sells.append(numout*sells['price'])
        persells.append(temp_sells)
        print('蘋果目前有', sells['num'], '顆')
    elif sel=='4': # 營業額與毛利
       print('今天有', len(persells), '筆交易')
       for i in range(len(persells)):
           print('第',i+1, '次賣了', persells[i][0], '顆', persells[i][1], '元')
       print('共賣了', sells['sell'], '顆')
       print('共賣了', sells['sell']*sells['price'], '顆')
    elif sel=='5':#庫存
        print('蘋果目前有', sells['num'], '顆')
    elif sel=='6':
        break
    else:
        print('wrong input')

