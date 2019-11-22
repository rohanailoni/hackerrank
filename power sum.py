



def f(x,n,num=1,sum=0):
    r=0
    p=num**n
    while p+sum<x:
        r+=f(x,n,num+1,sum+p)
        num+=1
        p=num**n
    if p+sum==x:
        r+=1
    return r

if __name__=="__main__":
    x=int(input())
    n=int(input())
    print(f(x,n,num=1,sum=0))
