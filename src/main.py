import time

file_table = []

def create_file():
    # Cria um novo arquivo no sistema de arquivos.
    name = input("Digite o nome do arquivo: ")
    content = input("Digite o conteúdo do arquivo: ")
    size = len(content)  # Variável que guarda o tamanho do arquivo

    # Verifica se o arquivo já existe
    for file in file_table:
        if file['name'] == name:
            print(f"\nArquivo '{name}' já existe.")
            return
        
    # Atualiza a tabela de arquivos
    file_entry = {
        'name': name,
        'size': size,
    }
    file_table.append(file_entry)
    print(f"\nArquivo '{name}' criado com sucesso!")

def read_file():
    # Lê o conteúdo de um arquivo específico.
    name = input("Digite o nome do arquivo a ser lido: ")

    # Encontra o arquivo na tabela de arquivos
    file_entry = next((file for file in file_table if file['name'] == name), None)

    if file_entry is None:
        print(f"\nArquivo '{name}' não encontrado.")
        return
    
    print(f"\nConteúdo do arquivo '{file_entry}'")

def delete_file():
    # Exclui um arquivo do sistema de arquivos.
    name = input("Digite o nome do arquivo a ser excluído: ")

    # Encontra o arquivo na tabela de arquivos
    file_entry = next((file for file in file_table if file['name'] == name), None)

    if file_entry is None:
        print(f"\nArquivo '{name}' não encontrado.")
        return
    
    # Remove da tabela de arquivos
    file_table.remove(file_entry)
    print(f"\nArquivo '{name}' excluído com sucesso!")

def print_file_table():
    # Imprime a tabela de arquivos.
    print("\nTabela de Arquivos:")
    print("-" * 50)
    if not file_table:
        print("Nenhum arquivo armazenado.")
    else:
        print(f"{'Nome':<15}{'Tamanho':<10}")
        for file in file_table:
            print(f"{file['name']:<15}{file['size']:<10}")
    print("-" * 50)

def main():
    # Função principal que exibe o menu e captura as escolhas do usuário.
    while True:
        print("Simulação de Sistema de Arquivos\n")
        print("[1] Criar Arquivo")
        print("[2] Ler Arquivo")
        print("[3] Excluir Arquivo")
        print("[4] Mostrar Tabela de Arquivos")
        print("[0] Sair\n")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            create_file()
            input("\nPressione Enter para continuar...")
        elif escolha == '2':
            read_file()
            input("\nPressione Enter para continuar...")
        elif escolha == '3':
            delete_file()
            input("\nPressione Enter para continuar...")
        elif escolha == '4':
            print_file_table()
            input("\nPressione Enter para continuar...")
        elif escolha == '0':
            print("\nEncerrando o programa...")
            time.sleep(2)
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            time.sleep(2)

if __name__ == "__main__":
    main()