numero_notas = 1
respuesta = "s"
total_alumnos = 0
while respuesta.lower() == "s":      # poner cadena en minusculas
    nombre = input("Nombre: ")
    nota_maxima = 0
    nota_minima = 101
    suma_notas = 0
    nota = -1
    for i in range(numero_notas):

        while nota < 0 or nota > 101:
            nota = float(input("Ingrese la nota #" + str(i+1) + ": "))
        suma_notas += nota
        if nota > nota_maxima:
            nota_maxima = nota
        if nota < nota_minima:
            nota_minima = nota
        nota = -1

    total_alumnos += 1

    nota_media = suma_notas / numero_notas
    print("Estadística de " + nombre)
    valor_equivalente = ""
    if nota_media < 40:
        valor_equivalente = "Insuficiente"
    elif nota_media < 60:
        valor_equivalente = "Suficiente"
    elif nota_media < 70:
        valor_equivalente = "Bien"
    elif nota_media < 80:
        valor_equivalente = "Notable"
    else:
        valor_equivalente = "Sobresaliente"

    print("-Nota media: " + str(nota_media) + " ("+valor_equivalente+")")
    respuesta = input("Se van a introducir más alumnos? [s/n] ")
