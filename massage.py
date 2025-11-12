service = "классический массаж" 
price = 2653
discount = 0.04
sessions = 10
total = price*sessions
print ("услуга" , service)
print ("стоимость" , price , "руб")
print ("сеансы" ,sessions)

if discount<=10:
    discount_session = price*discount
    final_total = total-discount_session

print ("скидка 3%" , discount_session , "руб")
print ("итоговая стоимость" , final_total , "руб")
print ("БЛАГОДАРИМ ЗА ПОКУПКУ")