n=int(input())

if n==1:
    print(n)
if n==0:
    print(n+1)

produto=n

while n>1:
    produto=produto*(n-1)
    n=n-1
    if n==1:
        print(produto)
        
