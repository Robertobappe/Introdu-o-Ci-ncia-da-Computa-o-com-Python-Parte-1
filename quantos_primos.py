def n_primos(n):
    p=1
    a=n-1
    b=2
    c=False
    d=False
    while a>2:
        while b<a:
            a/b
            if a%b==0:
                b+=1
                c=True
            else:
                d=True
                b+=1
        if c==False and d==True:
            p+=1
        b=2
        a=a-1
        c=False
        d=False
    return p
    
