#Código para escrever dados em um arquivo

from traceback import print_stack


try:
    arquivo = open("data/sistemas.txt", "w")
    continuar = True
    while continuar:
        os_name = input('Diga um OA (vazio para sair):')
        if not os_name:
            continuar = False
            continue
        arquivo.write(os_name)
    arquivo.close
except FileNotFoundError:
    print('Caminho não existe, favor verificar')
except Exception:
    print("Algo não esperado ocorreu:")
    print_stack()
finally:
    print("Chegamos no final!")