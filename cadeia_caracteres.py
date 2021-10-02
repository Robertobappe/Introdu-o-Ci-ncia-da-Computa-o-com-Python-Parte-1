c=int(input("digite a largura: "))
l=int(input("digite a altura: "))

i=1
j=1
largura='#'
#caracteres cheios 
while i<=l:
    while j<c:
        j+=1
        largura+='#'        
    print(largura, end="")
    print()
    i+=1







#última linha
print()
print(largura)
