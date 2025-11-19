def calculate_fine(zone, hours, has_permit):
    # Если есть разрешение
    if has_permit == True:
        return 0
   
    # Проверяем зоны
    if zone == "центр":
        if hours <= 1:
            return 500
        elif hours <= 3:
            return 1000
        else:
            return 2000
    
    elif zone == "окраина":
        if hours <= 2:
            return 300
        elif hours <= 5:
            return 600
        else:
            return 1200
    
    elif zone == "пригород":
        if hours <= 3:
            return 200
        elif hours <= 6:
            return 400
        else:
            return 800
    
    
    

fine1 = calculate_fine("центр", 2, False)
print("Центр, 2 ч, без разрешения:", fine1, "руб")