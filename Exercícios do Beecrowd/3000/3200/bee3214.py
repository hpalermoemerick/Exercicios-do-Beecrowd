entrada = list(map(int, input().split()))
num_refrigerantes,garrafas_encontradas,garrafas_necessarias = entrada
total = num_refrigerantes + garrafas_encontradas
bebeu = 0
while True:
    total = total - garrafas_necessarias + 1
    if total > 0:
        bebeu += 1
    else:
        break
print(bebeu)