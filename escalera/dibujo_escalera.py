num_pisos=int(input('Ingrese el número de pisos de su arbol:'))
print('---')
print('Este es su arbol:')
for i in range(num_pisos,0,-1):
    
    print(''*(num_pisos-i)+'#'*(num_pisos-i+1))# para que vaya disminuyendo en una unidad el numero de hastags por piso