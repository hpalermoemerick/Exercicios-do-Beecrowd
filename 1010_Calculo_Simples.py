cod1,num1,valor1 = input().split()
cod1,num1,valor1 = int(cod1),int(num1),float(valor1)

cod2,num2,valor2 = input().split()
cod2,num2,valor2 = int(cod2),int(num2),float(valor2)

peca1 = num1*valor1
peca2 = num2*valor2
total = peca1 + peca2
print(f'VALOR A PAGAR: R$ {total:.2f}')