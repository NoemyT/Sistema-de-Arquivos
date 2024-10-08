import time

# Tamanho do disco e inicialização
TAMANHO_DISCO = 32  # Número de blocos
disk = [{'char': None, 'pointer': None} for _ in range(TAMANHO_DISCO)]  # Representação do disco
free_blocks = [True] * TAMANHO_DISCO  # True indica que o bloco está livre

file_table = []

def print_disk():
    # Imprime o estado atual do disco
    print("\nEstado Atual do Disco:")
    print("-" * 40)
    print(f"{'Bloco':<8}{'Char':<8}{'Ponteiro':<8}")
    for i, block in enumerate(disk):
        char = block['char'] if block['char'] is not None else "Livre"
        pointer = str(block['pointer']) if block['pointer'] is not None else "-"
        print(f"{i:<8}{char:<8}{pointer:<8}")
    print("-" * 40)

def create_file():
    # Cria um novo arquivo no sistema de arquivos.
    name = input("Digite o nome do arquivo: ")
    content = input("Digite o conteúdo do arquivo: ")
    size = len(content)  # Tamanho do arquivo

    # Verifica se o arquivo já existe
    for file in file_table:
        if file['name'] == name:
            print(f"\nArquivo '{name}' já existe.")
            return

    # Verifica se há espaço livre suficiente
    total_free_blocks = sum(free_blocks)
    if total_free_blocks < size:
        print(f"\nEspaço insuficiente para criar o arquivo '{name}'.")
        return

    # Aloca blocos livres
    allocated_blocks = []
    free_indices = [i for i, free in enumerate(free_blocks) if free]
    for i in range(size):
        block_index = free_indices[i]
        allocated_blocks.append(block_index)
        free_blocks[block_index] = False

    # Escreve o conteúdo nos blocos alocados
    for i in range(size):
        block_index = allocated_blocks[i]
        char = content[i]
        if i < size - 1:
            next_block = allocated_blocks[i + 1]
        else:
            next_block = None  # Último bloco
        disk[block_index]['char'] = char
        disk[block_index]['pointer'] = next_block

    # Atualiza a tabela de arquivos
    file_entry = {
        'name': name,
        'size': size,
        'address': allocated_blocks[0]
    }
    file_table.append(file_entry)
    print(f"\nArquivo '{name}' criado com sucesso!")
    print_disk()

def read_file():
    # Lê o conteúdo de um arquivo específico.
    name = input("Digite o nome do arquivo a ser lido: ")

    # Encontra o arquivo na tabela de arquivos
    file_entry = next((file for file in file_table if file['name'] == name), None)

    if file_entry is None:
        print(f"\nArquivo '{name}' não encontrado.")
        return

    # Percorre os blocos do arquivo
    content = ''
    pointer = file_entry['address']
    while pointer is not None:
        block = disk[pointer]
        char = block['char']
        content += char
        pointer = block['pointer']

    print(f"\nConteúdo do arquivo '{name}': {content}")
    print_disk()

def delete_file():
    # Exclui um arquivo do sistema de arquivos.
    name = input("Digite o nome do arquivo a ser excluído: ")

    # Encontra o arquivo na tabela de arquivos
    file_entry = next((file for file in file_table if file['name'] == name), None)

    if file_entry is None:
        print(f"\nArquivo '{name}' não encontrado.")
        return

    # Libera os blocos alocados
    pointer = file_entry['address']
    while pointer is not None:
        next_pointer = disk[pointer]['pointer']
        # Limpa o bloco
        disk[pointer]['char'] = None
        disk[pointer]['pointer'] = None
        free_blocks[pointer] = True
        pointer = next_pointer

    # Remove da tabela de arquivos
    file_table.remove(file_entry)
    print(f"\nArquivo '{name}' excluído com sucesso!")
    print_disk()

def print_file_table():
    # Imprime a tabela de arquivos.
    print("\nTabela de Arquivos:")
    print("-" * 40)
    if not file_table:
        print("Nenhum arquivo armazenado.")
    else:
        print(f"{'Nome':<15}{'Tamanho':<10}{'Endereço':<10}")
        for file in file_table:
            print(f"{file['name']:<15}{file['size']:<10}{file['address']:<10}")
    print("-" * 40)

def main():
    # Função principal que exibe o menu e captura as escolhas do usuário.
    while True:
        print("\nSimulação de Sistema de Arquivos\n")
        print("[1] Criar Arquivo")
        print("[2] Ler Arquivo")
        print("[3] Excluir Arquivo")
        print("[4] Mostrar Tabela de Arquivos")
        print("[5] Mostrar Estado do Disco")
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
        elif escolha == '5':
            print_disk()
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
