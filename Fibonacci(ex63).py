print("Sequência de Fibonacci")
print("-"*30)
n = int(input('Quantos termos deseja mostrar na sequência? '))
q = int(input('Digite o número que deseja saber se está na sequência: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2),end=' ')

listaf = [t1,t2]
cont = 3
while cont <= n:
    t3 =  t1 + t2
    print('-> {}'.format(t3),end=' ')
    t1 = t2
    t2 = t3
    listaf.append(t3)
    cont += 1
print("FIM")

print(" ")
if q in listaf:
    print("O número {} está na sequência.".format(q))

else:
    print("O número {} não está na sequência.".format(q))