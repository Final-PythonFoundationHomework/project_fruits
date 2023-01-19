def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    sum=0
    fruits=[]
    price=[]
    f=open(data).read()
    arr1=f.split('\n')
    for i in arr1:
        fruits.append(i[:i.find(',')])
    for i in arr1:
        price.append(i[(i.find(',')+1):])
    price.remove(price[0])
    price.remove(price[-1])
    for i in price:
        sum+=float(i)
    return sum
print(get_total_price('fruits.csv'))