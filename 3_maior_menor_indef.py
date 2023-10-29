#Função retorna o maior número da lista
def f_maior(lista):
    return max(lista)

#Função retorna o menor número da lista
def f_menor(lista):
    return min(lista)

def main():

    lista = []

    while True:
        x = (int(input()))  #Entrada de Dados
        if x != 0:  #Se o número positivo não for zero, é adicionado à lista
            lista.append(x)
        if x <= 0: break    #Se o número for menor ou igual a zero, para o loop
        
    #Saída de Dados        
    print(f'{f_maior(lista)}') 
    print(f'{f_menor(lista)}')


if __name__ == '__main__':
    main()
