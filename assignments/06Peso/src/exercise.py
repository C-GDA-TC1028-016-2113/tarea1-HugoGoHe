def main():
    pesoI = float(input("Dame el peso inicial: "))
    pesoF = float(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))

    resta = pesoI - pesoF
    print("Lo que debes bajar por mes es: " + str(resta/meses))


if __name__ == '__main__':
    main()
