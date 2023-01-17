def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    # your code here
    s=[]
    name=[]
    # your code here
    f=open(data,mode='r').read()
    arr=f.split('\n')
    for i in arr[1:-1]:
        s.append(float(i.split(',')[1]))
        name.append(i.split(',')[0])
    ind=max(s)
    return name[s.index(ind)]
print(get_expensive_fruit('fruits.csv'))

