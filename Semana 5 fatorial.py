def fatorial(n):
    fat = 1
    while (n>1):
        fat=fat*n
        n=n-1
    return fat

def num_binomial(n,k):
    return fatorial(n)/(fatorial(k)*fatorial(n-k))

def testa_fatorial():
    if fatorial(1)==1:
        print("Funciona pra 1")
    else:
        print("Nao funciona pra 1")
    if fatorial(2)==2:
        print("Funciona pra 2") 
    else:
        print("Não funciona pra 2")
    if fatorial(0)==1:
        print("Funciona pra 0") 
    else:
        print("Não funciona pra 0")
