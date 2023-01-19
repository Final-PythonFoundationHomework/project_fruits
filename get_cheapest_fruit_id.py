def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    s=[]
    # your code 
    f=open(data,mode='r').read()
    arr=f.split('\n')
    for i in arr[1:-1]:
        s.append(float(i.split(',')[1]))
    ind=min(s)
    return s.index(ind)
print(get_cheapest_fruit_id('fruits.csv'))