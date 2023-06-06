bolinhas = int(input())
galhos = int(input()) 
falta = galhos // 2 - bolinhas
if falta > 0:
    print(f"Faltam {falta} bolinha(s)")
else:
    print("Amelia tem todas bolinhas!")