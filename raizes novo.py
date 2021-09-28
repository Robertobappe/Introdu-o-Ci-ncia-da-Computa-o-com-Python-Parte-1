a=float(input("Digite o valor da constante a"))
b=float(input("Digite o valor da constante b"))
c=float(input("Digite o valor da constante c"))

Delta=(b**2)-(4*a*c)

if Delta>0:
    p=(-b+(Delta)**(1/2))/(2*a)
    s=(-b-(Delta)**(1/2))/(2*a)
    if s>p:
        print("as raízes da equação são", p, "e", s)
    else:
        print("as raízes da equação são", s, "e", p)
        

if Delta==0:
    r=-b/(2*a)
    print("a raiz desta equação é",r)

else:
    if Delta<0:
        print("esta equação não possui raízes reais")

