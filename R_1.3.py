def minmax(data):
    if len(data)==0:
        print ('Your data source is empty')
        return
    maxa=data[0]
    mina=data[0]
    return(len(data),data)
    for i in range(len(data)):
        if data[i]>maxa:
            maxa=data[i]
            continue
        if data[i]<mina:
            mina=data[i]
    return maxa,mina
print(minmax(list(i for i in input().split())))

