import pandas as pd

try:
    df = pd.read_csv('dados_loja.txt', sep=';', index_col=False)
except FileNotFoundError:
    df = pd.DataFrame(columns=['ID', 'Produto', 'Preço', 'Quantidade', 'Cliente'])

def salvar_dados():
    df.to_csv('dados_loja.txt', sep=';', index=False)

def adicionar_produto():
    id = int(input("Digite o ID do produto: "))
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    cliente = input("Digite o nome do cliente: ")
    new_data = {'ID': id, 'Produto': produto, 'Preço': preco, 'Quantidade': quantidade, 'Cliente': cliente}
    global df
    df = df.append(new_data, ignore_index=True)
    salvar_dados()
    print("Produto adicionado com sucesso!\n")

def ler_produtos():
    print("Listando todos os produtos:\n", df)

def atualizar_produto():
    id = int(input("Digite o ID do produto que deseja atualizar: "))
    index = df.index[df['ID'] == id].tolist()
    if not index:
        print("Produto não encontrado!")
        return
    produto = input("Digite o novo nome do produto (pressione enter para manter o atual): ")
    preco = input("Digite o novo preço do produto (pressione enter para manter o atual): ")
    quantidade = input("Digite a nova quantidade do produto (pressione enter para manter o atual): ")
    cliente = input("Digite o novo nome do cliente (pressione enter para manter o atual): ")
    if produto:
        df.loc[index[0], 'Produto'] = produto
    if preco:
        df.loc[index[0], 'Preço'] = float(preco) if preco else df.loc[index[0], 'Preço']
    if quantidade:
        df.loc[index[0], 'Quantidade'] = int(quantidade) if quantidade else df.loc[index[0], 'Quantidade']
    if cliente:
        df.loc[index[0], 'Cliente'] = cliente
    salvar_dados()
    print("Produto atualizado com sucesso!\n")

def deletar_produto():
    id = int(input("Digite o ID do produto que deseja deletar: "))
    index = df.index[df['ID'] == id].tolist()
    if not index:
        print("Produto não encontrado!")
        return
    df.drop(index, inplace=True)
    salvar_dados()
    print("Produto deletado com sucesso!\n")

def menu():
    while True:
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Sair")
        opcao = input("Escolha uma opcao: ")
        
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            ler_produtos()
        elif opcao == '3':
            atualizar_produto()
        elif opcao == '4':
            deletar_produto()
        elif opcao == '5':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
