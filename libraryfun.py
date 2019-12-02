def displayAvailablebooks():
    print("1 Show Record:")
    print("2 Add Book:")
    print("3 Withdraw Book:")
    print("4 Price of Book:")
    x = int(input("your option:"))
    return x

def insertItem(book):
    bname = input("Book name:")
    bqty = int(input("Total book:"))
    bprice = int(input("price:"))
    
    if bname in book:
        q=stock[bname][0]+bqty
        p=stock[bname][1]+bprice
        stock[bname][0] = q
        stock[bname][1] = p
    else:
        stock[bname][0]=bqty
        stock[bname][1]=bprice
        
def dispatchItem(stock):
    bname=input("product name:")
    bqty = int(input("product qty:"))
    bprice = int(input("product price:"))
    if bname in stock:
        q = stock[bname]
        if q>=bqty:
            stock[bname][0] = q-bqty
        else:
            print("Not sufficient qty")
    else:
            print("Product not avilable")

def priceOfTotal(stock):
    bprice = int
    q = stock[bprice][1]
    for n in range(bprice):
        stock[bprice] = q+bprice
        print(n)
        return n

    
