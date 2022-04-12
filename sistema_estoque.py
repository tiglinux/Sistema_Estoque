import json

vetorProduto = []
qtd = 0


def main():
    codigo = 0
    valorVenda = 0.25

    while True:
        menuInterface()
        opcao = int(input("\nEscolha uma opção: "))

        if (opcao == 0):
            print("Aplicação encerrada")
            break
        while (opcao == 1):
            if (opcao == 1):
                nomeProduto = str(input("\nInforme o nome do Produto: "))
                valorCompra = float(input("Informe o valor de compra: R$"))
                qtd = int(input("Informe a quantidade no estoque: "))
                codigo += 1
                valorVenda = (valorVenda * valorCompra) + valorCompra
                vetorProduto.append([codigo, nomeProduto, valorCompra, valorVenda, qtd])  # Aqui eu incremento no vetor

                continuarCadastro = str(input("Deseja continuar o Cadastro? S ou N : "))

                if (continuarCadastro == 'N'):  # Se a opção é N então chama a interface de MENU
                    break
                elif (continuarCadastro == 'S'):
                    continue

        if (opcao == 2):
            relatorioProdutos()

        if (opcao == 3):
            relatorioEstoqueBaixo()
        if (opcao == 4):
            exportarDados()


def relatorioProdutos():
    print("\n--- Relatório de Produtos ---\n")
    for i in sorted(vetorProduto):
        print(i)


def relatorioEstoqueBaixo():
    print("\n--- Relatório de Estoque Baixo ---\n")
    for n in vetorProduto[qtd]:
        if n <= 5:
            print(n)


def exportarDados():
    print(json.dumps(vetorProduto,indent=4))                    #Aqui eu apresento para o usuário o JSOn
    with open('exportarDados.json','w') as f:                   #Aqui eu converto e exporto o arquivo para JSON
        json.dump(vetorProduto,f,ensure_ascii=False, indent=4)

def menuInterface():
    print("\n---Varejão do João---\n")
    print("[1] Cadastrar de produto\n" +
          "[2] Relatório de produtos\n" +
          "[3] Relatório de Estoque Baixo\n" +
          "[4]Exportar dados\n" +
          "[0] Sair\n")


main()
