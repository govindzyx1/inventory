from stockFunction import *
stock = {}

y='y'
while y=='y':
    option = showOption()
    print(option)

    if option==1:
        print("ok")
        print(stock)
    elif option==2:
        insertItem(stock)
    elif option==3:
        print("Hi")
        dispatchItem(stock)
    elif option==4:
        print("Hi Govind")
        priceOfTotal(stock)
    elif option==5:
        print("Calculate your bill:")
        billing(stock)
    y = input("do you want to continue y/n?")


#price and d=show total value of product
