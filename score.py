def get_grade(score):
    if score >= 90:
        return "отлично"
    elif score >= 75:
        return "хорошо"
    elif score >= 65:
        return "удовлетворительно"
    else:
        return "Неудовлетворительно"
    

grade1 = get_grade(95)
print("95 баллов:", grade1)  # должно быть "Отлично"

grade2 = get_grade(82)
print("82 балла:", grade2)  # должно быть "Хорошо"

grade3 = get_grade(65)
print("65 баллов:", grade3)  # должно быть "Удовлетворительно"

grade4 = get_grade(45)
print("45 баллов:", grade4)  # должно быть "Неудовлетворительно"

grade5 = get_grade(100)
print("100 баллов:", grade5)
   
