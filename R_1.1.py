def is_multiple(n,m):
    if m%n==0:
        return True
    else:
        return False
    
m,n=map(int,input().split())
print(is_multiple(m,n))
