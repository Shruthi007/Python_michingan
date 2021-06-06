n=int(input())

for i in range(n):
    x=[]
    c=1
    r=int(input())
    p=(input().split())
    for j in p:
        x.append(int(j))
    for k in range(0,len(x)-1):
        if x[k]>x[k+1]:
            c=c+1
        else:
            x[k+1]=x[k]-1
    
    print(c)
