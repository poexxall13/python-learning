def usd_to_rub(usd, exchange_rate):
    rubles: float = usd*exchange_rate
    return rubles

rub1 = usd_to_rub(100, 95)
print("100 USD =", rub1, "руб")  # должно быть 9500

rub2 = usd_to_rub(50, 100)
print("50 USD =", rub2, "руб")