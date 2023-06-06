def ehBissexto(ano):
    if (ano%400==0) or (ano%4==0 and ano%100!=0):
        return True
    return False

def inicio():    
    n = int(input())
    JUPITER = 11.9
    SATURNO = 29.6
    DIA_INICIAL = 21
    MES_INICIAL = 12
    ANO_INICIAL = 2020
    diasJupiter = 0
    dataJupiter = ""
    diasSaturno = 0
    dataSaturno = ""
    anosBissextosJupiter = 0
    anosBissextosSaturno = 0
    jpt = []
    sat = []
    
    #jupiter =============================================
    ano = 2021
    fim = (2020 + 11*n + 1)
    for i in range(ano,fim+1):
        if ehBissexto(i):
            anosBissextosJupiter += 1
        jpt.append(i)
    diasJupiter = n*(365*JUPITER + anosBissextosJupiter)
    
    aux = diasJupiter
    anosJpt = 0
    for i in jpt:
        if ehBissexto(i):
            aux -= 366
        else:
            aux -= 365
        anosJpt += 1  
        
    #saturno =============================================
    ano = 2021
    fim = (2020 + 29*n + 1)
    for i in range(ano,fim+1):
        if ehBissexto(i):
            anosBissextosSaturno += 1
        sat.append(i)    
    diasSaturno = n*(365*SATURNO + anosBissextosSaturno)
    
    
    
    print(f'Dias terrestres para Jupiter = {diasJupiter}')
    print(f'Dias terrestres para Jupiter = {dataJupiter}')        
    print(f'Dias terrestres para Saturno = {diasSaturno}')        
    print(f'DDias terrestres para Saturno = {dataSaturno}')        

    # Dias terrestres para Jupiter = 4346
    # Data terrestre para Jupiter: 2032-11-14
    # Dias terrestres para Saturno = 10811
    # Data terrestre para Saturno: 2050-07-28
inicio()