import numpy as np
from sympy import *
print(""" _____  _    ____  _   _ ___ _   _ _    _  ___    ____  _____ ____  _   _   __  
|_   _|/ \  |  _ \| | | |_ _| \ | | | | |/ _ \   |  _ \| ____/ ___|| | | |   \ \ 
  | | / _ \ | |_) | |_| || ||  \| | |_| | | | |  | | | |  _| \___ \| | | |   (_) |
  | |/ ___ \|  __/|  _  || || |\  |  _  | |_| |  | |_| | |___ ___) | |_| |    _| |
  |_/_/   \_\_|   |_| |_|___|_| \_|_| |_|\___/   |____/|_____|____/ \___/    ( ) |
                                                                             |/_/ 
 \n""")
print("---UTILISATION DES OPERATEURS---\n")
print("""    
    + : Opérateur d'addition. 

    - : Opérateur de soustraction.

    * : Opérateur de multiplication.

    / : Opérateur de division.

    ** : Opérateur de puissance.   

    sin() : Fonction sinus.

    cos() : Fonction cosinus.

    tan() : Fonction tangente.

    exp() : Fonction exponentielle.

    ln()  : Logarithme naturel.

    sqrt(): Racine carre.

    abs() : Valeur absolue.
""")
x = symbols('x')  
n = symbols('n')
# la fonction fn(x)
F=input("ENTREZ UNE FONCTION fn(x)= ")
interinf=input("ENTREZ LA BORNE INFERIEURE DE LA DF: ")
if interinf == "-oo":
    interinf=-5
else:
    interinf=int(interinf)
intersup=input("ENTREZ LA BORNE SUPERIEURE DE LA DF: ")
if intersup == "+oo":
    intersup=5
else:
    intersup=int(intersup)
F=parse_expr(F)
print("TRAINTEMENT...")
def fn(s,t):
     values = {x: t, n: s}
     fa = F.subs(values)
     return fa

#la fonction f(x) 
def f(x): 
    return limit(fn(n,x), n,oo)
#la fonction |fn(x)-f(x)|
def hn(n,x):
        return fn(n,x)-f(x)

print("--------DETERMINATION DE LA CONVERGENCE SIMPLE ...\n\n")
if f(1)==oo:
    print("LA FOCTION N'EST PAS SIMPLEMENT CONVERGENTE")

else:   
    #Determination de sup|fn(x)-f(x)|
   print("--------DETERMINATION DE SUP|fn(x)-f()| ...\n\n")   
   supx = interinf
   for m in np.arange(interinf,intersup,0.1):
        if hn(100,m)>hn(100,supx):
            supx=m

    #la limite du sup lorsque n tend ver l'infini  
   sup=hn(n,supx)    
   l=limit(sup,n,oo)
   if l==0:
            print("LA FONCTION EST UNIFORMEMENT CONVERGENTE")
   else:
            print("LA FONCTION N'EST PAS UNIFORMENT CONVERGENTE")