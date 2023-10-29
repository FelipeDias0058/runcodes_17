

def main():

    #Entrada de Dados
    capital = float(input())
    taxa_juros = float(input())

    #Definição das variáveis que serão calculadas
    juros = (taxa_juros / 100.0) + 1
    rendimento = capital
    anos = 0

    #Faz o loop do cálculo de juros até que
    #o valor do rendimento seja o dobro do capital
    while rendimento <= (capital * 2):
        rendimento *= juros
        anos += 1

    #Saída de Dados
    print(anos)

if __name__ == '__main__':
    main()
