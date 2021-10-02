a=False
b=False
c=False

def computador_escolhe_jogada(n,m):
    i=1
    if (n-i)%(m+1)==0:
        
        return i
          
    else:
        while i<=m:
            
            if (n-i)%(m+1)==0:
                                
                return i
                i+=1
            else:
                i+=1
    if i>m:
        
        return m

def usuario_escolhe_jogada(n,m):
    x=input("Quantas peças você vai tirar? ")
    x=int(x)
       
    if x<=m and x>0 and x<=n:
        
        return x
    
    else:
        if n<=m and x>n:
            x=int(input())
           
            return x
        else:
            while x<=0 or x>m:
                x=input()
                x=int(x)
                if x>0 and x<=m:
                    
                    return x


def partida():
    n=input("Quantas peças? ")
    n=int(n)
    m=input("Limite de peças por jogada? ")
    m=int(m)
    global a
    global b
    global c
    if n%(m+1)==0:
        print("\nVoce começa!\n")
        u=usuario_escolhe_jogada(n,m)
        a=True
        print("Voce tirou",u, "peças")
        n=n-u
                                                  
    else:
        print("\nComputador começa!\n")
        c=computador_escolhe_jogada(n,m)
        print("Computador tirou", c, "peças")
        n=n-c
        
    while n>0:
        
        if a==True:
            c=computador_escolhe_jogada(n,m)
            print("Computador tirou", c, "peças.")
            n=n-c
            if n!=0:
                u=usuario_escolhe_jogada(n,m)
                print("Voce tirou",u, "peças")
                n=n-u
            else:
                print("Fim de jogo! O computador ganhou!")
                b=True      
        else:
            u=usuario_escolhe_jogada(n,m)
            print("Voce tirou",u, "peças")
            n=n-u
            if n!=0:
                c=computador_escolhe_jogada(n,m)
                print("Computador tirou", c, "peças")
                n=n-c
            else:
                print("Fim de jogo! O computador ganhou!")
                c=True
    if n==0 and b==False or c==False:
        print("Fim de jogo! O computador ganhou!")
            

y=input("Bem-vendo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato ")
y=int(y)


if y==1:
    print("\nVoce escolheu uma partida!")
    partida()
else:
    print("\nVoce escolheu um campeonato!\n")
    print("*** Rodada 1 ***\n")
    partida()

    print("\n*** Rodada 2 ***\n")
    partida()

    print("\n*** Rodada 3 ***\n")
    partida()
    print("\n*** Final do campeonato! ***\n")
    print("Placar: Você 0 X 3 Computador")




















