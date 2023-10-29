#Função calcula a média da lista
def f_media(lista):
    return sum(lista) / len(lista)

def main():

    lista = []

    while True:
        x = (int(input()))  #Entrada de Dados
        if x > 0:            
            lista.append(x)  #Se o número positivo não for zero, é adicionado à lista
        if x <= 0: break    #Se o número for menor ou igual a zero, para o loop
        
            
    print(f'{f_media(lista):.2f}')  #Saída de Dados


if __name__ == '__main__':
    main()
