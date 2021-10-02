l=int(input("digite a largura: "))
c=int(input("digite a altura: "))

i=1
j=1
largura='#'

while i<=c:
    if i==1 or i==c:
        while j<l:
            j+=1
            largura+='#'
        print(largura, end="")
        print()
        i+=1
        j=1
        largura='#'
    else:
        while j<l-1:
            j+=1
            largura=largura+' '
        largura+='#'
        
        print(largura, end="")
        print()
        i+=1
        j=1
        largura='#'

    



    
