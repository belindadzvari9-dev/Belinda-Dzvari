#python currrency convertor program

amount  =   float(input("enter the amount you would like to cornvert"))
currency = input("enter the currency you would like to cornvert:    USD/ZW")

if currency.upper() == "USD":
    amount = amount * 26.67
    currency = "ZW"
    print(f"your cornverted amount is {currency}{amount:.2f}")
elif currency.upper() == "ZW":
    amount  = amount /   26.67
    currency = "USD"
    print(f"your cornverted amount is {currency}{amount:.2f}")
else:
    print(f"your cornverted amount is {currency}{amount:.2f}")

