from random import randint

P = 13172937415361
G = 9
print('El valor de P es: %d'%(P))
print('El valor de G es: %d'%(G))
 
a = 4
print('La llave secreta de Alice es: %d'%(a))
A = int(pow(G,a,P))

b = 3
print('La llave secreta de Bob es: %d'%(b))
B = int(pow(G,b,P)) 
 
ka = int(pow(B,a,P))
kb = int(pow(A,b,P))
print('La llave secreta calculada por Alice es: %d'%(ka))
print('La llave secreta calculada por Bob es: %d'%(kb))
