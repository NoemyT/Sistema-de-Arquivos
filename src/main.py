import os
import time
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Tamanho do disco e inicialização
TAMANHO_DISCO = 32  # Número de blocos
disk = [{'char': None, 'pointer': None} for _ in range(TAMANHO_DISCO)]  # Representação do disco

file_table = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_disk():
    # Imprime o estado atual do disco
    console.print("\n[bold cyan]Estado Atual do Disco:[/bold cyan]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Bloco", style="dim", width=6)
    table.add_column("Char", width=8)
    table.add_column("Ponteiro", justify="right")
    for i, block in enumerate(disk):
        char = block['char'] if block['char'] is not None else "[green]Livre[/green]"
        pointer = str(block['pointer']) if block['pointer'] is not None else "-"
        table.add_row(str(i), char, pointer)
    console.print(table)

def create_file():
    # Cria um novo arquivo no sistema de arquivos.
    name = console.input("[bold green]Digite o nome do arquivo:[/bold green] ")
    content = console.input("[bold green]Digite o conteúdo do arquivo:[/bold green] ")
    size = len(content)  # Tamanho do arquivo

    # Verifica se o arquivo já existe
    for file in file_table:
        if file['name'] == name:
            console.print(f"\n[red]Arquivo '{name}' já existe.[/red]")
            return

    # Verifica se há espaço livre suficiente
    total_free_blocks = sum(1 for block in disk if block['char'] is None)
    if total_free_blocks < size:
        console.print(f"\n[red]Espaço insuficiente para criar o arquivo '{name}'.[/red]")
        return

    # Aloca blocos livres
    allocated_blocks = []
    for i, block in enumerate(disk):
        if block['char'] is None:
            allocated_blocks.append(i)
            if len(allocated_blocks) == size:
                break

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
    console.print(f"\n[green]Arquivo '{name}' criado com sucesso![/green]")
    print_disk()

def read_file():
    # Lê o conteúdo de um arquivo específico.
    name = console.input("[bold green]Digite o nome do arquivo a ser lido:[/bold green] ")

    # Encontra o arquivo na tabela de arquivos
    file_entry = next((file for file in file_table if file['name'] == name), None)

    if file_entry is None:
        console.print(f"\n[red]Arquivo '{name}' não encontrado.[/red]")
        return

    # Percorre os blocos do arquivo
    content = ''
    pointer = file_entry['address']
    while pointer is not None:
        block = disk[pointer]
        char = block['char']
        content += char
        pointer = block['pointer']

    panel = Panel(f"[bold cyan]{content}[/bold cyan]", title=f"Conteúdo do arquivo '{name}'", expand=False)
    console.print(panel)
    print_disk()

def delete_file():
    # Exclui um arquivo do sistema de arquivos.
    name = console.input("[bold green]Digite o nome do arquivo a ser excluído:[/bold green] ")

    # Encontra o arquivo na tabela de arquivos
    file_entry = next((file for file in file_table if file['name'] == name), None)

    if file_entry is None:
        console.print(f"\n[red]Arquivo '{name}' não encontrado.[/red]")
        return

    # Libera os blocos alocados
    pointer = file_entry['address']
    while pointer is not None:
        next_pointer = disk[pointer]['pointer']
        # Limpa o bloco
        disk[pointer]['char'] = None
        disk[pointer]['pointer'] = None
        pointer = next_pointer

    # Remove da tabela de arquivos
    file_table.remove(file_entry)
    console.print(f"\n[green]Arquivo '{name}' excluído com sucesso![/green]")
    print_disk()

def print_file_table():
    # Imprime a tabela de arquivos.
    console.print("\n[bold cyan]Tabela de Arquivos:[/bold cyan]")
    if not file_table:
        console.print("[yellow]Nenhum arquivo armazenado.[/yellow]")
    else:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Nome", style="dim", width=15)
        table.add_column("Tamanho", justify="right")
        table.add_column("Endereço", justify="right")
        for file in file_table:
            table.add_row(file['name'], str(file['size']), str(file['address']))
        console.print(table)

def main():
    # Função principal que exibe o menu e captura as escolhas do usuário.
    while True:
        clear_screen()
        console.rule("[bold blue]Simulação de Sistema de Arquivos[/bold blue]", style="blue")
        console.print("[bold magenta][1][/bold magenta] Criar Arquivo")
        console.print("[bold magenta][2][/bold magenta] Ler Arquivo")
        console.print("[bold magenta][3][/bold magenta] Excluir Arquivo")
        console.print("[bold magenta][4][/bold magenta] Mostrar Tabela de Arquivos")
        console.print("[bold magenta][5][/bold magenta] Mostrar Estado do Disco")
        console.print("[bold magenta][0][/bold magenta] Sair\n")
        escolha = console.input("[bold green]Escolha uma opção:[/bold green] ")

        if escolha == '1':
            create_file()
            console.input("\nPressione Enter para continuar...")
        elif escolha == '2':
            read_file()
            console.input("\nPressione Enter para continuar...")
        elif escolha == '3':
            delete_file()
            console.input("\nPressione Enter para continuar...")
        elif escolha == '4':
            print_file_table()
            console.input("\nPressione Enter para continuar...")
        elif escolha == '5':
            print_disk()
            console.input("\nPressione Enter para continuar...")
        elif escolha == '0':
            console.print("\n[bold red]Encerrando o programa...[/bold red]")
            time.sleep(1)
            break
        else:
            console.print("\n[red]Opção inválida! Tente novamente.[/red]")
            time.sleep(1)

if __name__ == "__main__":
    main()
