def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    s=[]
    name=[]
    # your code here
    f=open(data,mode='r').read()
    arr=f.split('\n')
    for i in arr[1:-1]:
        name.append(i.split(',')[0])
    return name
print(get_frutis_name('fruits.csv'))
    