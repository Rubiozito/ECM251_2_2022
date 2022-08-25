#Código para escrever dados em um arquivo

arquivo = open("data/sistemas.txt", "w")
continuar = True
while continuar:
    os_name = input('Diga um OA (vazio para sair):')
    if not os_name:
        continuar = False
        continue
    arquivo.write(os_name)
arquivo.close