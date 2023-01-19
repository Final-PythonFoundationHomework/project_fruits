def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    s=[]
    name=[]
    # your code here
    f=open(data,mode='r').read()
    arr=f.split('\n')
    for i in arr[1:-1]:
        s.append(float(i.split(',')[1]))
        name.append(i.split(',')[0])
    ind=min(s)
    return name[s.index(ind)]
print(get_cheapest_fruit('fruits.csv'))