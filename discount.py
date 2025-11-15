def calculate_final_price(price, discount):
    discount_rub: float = price * (discount/100)
    total_price: int = price - discount_rub
    return total_price

item1 = calculate_final_price(1000,10)
print("товар1", item1, "руб")

item2 = calculate_final_price(5000, 25)
print("Товар 2:", item2, "руб")

item3 = calculate_final_price(300, 50)
print("Товар 3:", item3, "руб")