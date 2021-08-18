def main():
    #escribe tu código abajo de esta línea
    calificaciones = []
    for i in range(0,4):
        calificaciones.append(float(input("Calificación de la materia: ")))
    promedio = sum(calificaciones)/4
    print("El promedio es: " + str(promedio))

if __name__ == '__main__':
    main()
