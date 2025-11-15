def get_season(month):
    if month == 12:
        return "Зима"
    elif month == 1:
        return "Зима"
    elif month == 2:
        return "Зима"
    elif month == 3:
        return "Весна"
    elif month == 4:
        return "Весна"
    elif month == 5:
        return "Весна"
    elif month == 6:
        return "Лето"
    elif month == 7:
        return "Лето"
    elif month == 8:
        return "Лето"
    elif month == 9:
        return "Осень"
    elif month == 10:
        return "Осень"
    elif month == 11:
        return "Осень"
    else:
        return "Ошибка! Месяц должен быть от 1 до 12"

# Проверка всех сезонов:
season1 = get_season(1)
print("Месяц 1:", season1)  # Зима

season2 = get_season(4)
print("Месяц 4:", season2)  # Весна

season3 = get_season(7)
print("Месяц 7:", season3)  # Лето

season4 = get_season(10)
print("Месяц 10:", season4)  # Осень

season5 = get_season(12)
print("Месяц 12:", season5)  # Зима

# Проверка ошибки:
season6 = get_season(15)
print("Месяц 15:", season6)