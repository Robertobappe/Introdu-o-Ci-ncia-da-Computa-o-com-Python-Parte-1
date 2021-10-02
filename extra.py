n=int(input())
L=[]
l=[]
i=0
j=0
while n!=0:
    L.append(n)
    n=int(input())
    if n==0:
        a=len(L)
        a=a-1
        while a>=0:
            l.append(L[a])
            a=a-1
        b=len(l)
        b=b-1
while j<=b:
    print(l[j])
    j+=1

            
        
            
            
    
