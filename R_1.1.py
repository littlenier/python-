def is_multiple(n,m):
    if m==0:
        return False
    if n%m==0:
        return True
    else:
        return False
    
n,m=map(int,input().split())
print(is_multiple(n,m))

____________________________________
def is_multiple(n,m):
    if m==0:
        return False
    return(n%m==0)
    
n,m=map(int,input().split())
print(is_multiple(n,m))
