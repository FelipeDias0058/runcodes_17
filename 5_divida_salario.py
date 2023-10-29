
def main():

    #Entrada de Dados
    v_salario = float(input())
    v_divida = float(input())

    mes = 10
    ano = 2016
    taxa_juros = 0.15  
    aumento_salario = 0.05
  

    while v_divida <= v_salario:
        v_divida += v_divida * taxa_juros 

        if mes == 3:
            v_salario += v_salario * aumento_salario
            
        mes += 1

        if mes > 12:
            mes = 1
            ano += 1

        if v_divida > v_salario: break

    #Saída de Dados
    print(f'{mes}/{ano}')

if __name__ == '__main__':
    main()
