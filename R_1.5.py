from time import time
def su(n):
    a=time()
    sums=sum([i*i for i in range(1,n+1) ])
    b=time()
    return sums,b-a

print(su(int(input())))


        
