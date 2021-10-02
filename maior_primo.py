def maior_primo(k):
    p=3
    i=4
    if k==1 or k==2 or k==3:
            return k
    while i<=k:
        if i%2!=0 and i%3!=0:
            p=i
            i+=1
        
        else:
            i+=1

    return p
        
        
