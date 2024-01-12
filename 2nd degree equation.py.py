def delta(a, b, c): #criação da função / function creation
    y = b**2        # variaveis y e z criadas para evitar bugs / y and z variables created to avoid bugs
    z = 4*a         #.....
    x = y - (z * c) #calculo de Delta / Delta calculation
    x1 = (-b + x**(1/2) ) / (2*a)  # calculo valor de x1 / calculate value of x1
    x2 = (-b - x**(1/2) ) / (2*a)  # calculo valor de x2 / calculate value of x2
    return f'delta {x}', f'x1 {x1}' , f'x2 {x2}' # retorno dos valores calculados / return of calculated values

res = delta()  #variavel de resposta / response variable
print(res)

    