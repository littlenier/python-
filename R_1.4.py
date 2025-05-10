from time import time
def su(n):
    sums=0
    a=time()
    for i in range(1,n+1):
        sums+=i*i
    b=time()
    return sums,b-a
print(su(int(input())))


        
