#A função inverte os dígitos do número digitado
def f_inverter(num):
    inverso = 0
    resto = 0
    while (num != 0):
        resto = num % 10
        inverso = inverso * 10 + resto
        num //= 10
    return inverso #Retorna os dígitos na ordem inversa
        
    

def main():

    #Entrada de Dados
    num_int = int(input())

    #Saída de Dados
    print(f_inverter(num_int))


if __name__ == '__main__':
    main()
    
