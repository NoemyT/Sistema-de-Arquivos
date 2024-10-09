# 🗄️Sistema de Arquivos 🚀

## 👩‍💻 Informações da Equipe 👨‍💻

| 🌟 Nome                   | 🎓 Matrícula  |
|---------------------------|--------------|
| Caio Teixeira da Silva    | 22112243     |
| Noemy Torres Pereira      | 22112110     |

**🏫 Universidade Federal de Alagoas (UFAL)**  
**🏛️ Campus Arapiraca**  
**📚 Disciplina: Sistemas Operacionais**  
**💻 Curso: Ciência da Computação**  
**👨‍🏫 Professor: Tércio de Morais**

---

## 📝 Descrição do Projeto 📂

### 🖥️ Área

Este projeto está inserido na disciplina de **Sistemas Operacionais**, com foco no gerenciamento de sistemas de arquivos e memória.

### 📄 Tema

Desenvolvimento de uma **simulação de sistema de arquivos** que permite a criação, leitura e exclusão de arquivos, maximizando o uso da memória e gerenciando a fragmentação que ocorre durante essas operações.

---

## 🎯 Objetivos da Implementação 🎯

   🛠️ **Implementar um sistema de arquivos com lista encadeada**:
   - Simular o armazenamento de arquivos em blocos de memória, cada um contendo um caractere e um ponteiro para o próximo bloco.
   - Gerenciar a memória livre usando um mapa de bits ou encadeamento.

   💾 **Gerenciar eficientemente a memória**:
   - Permitir a criação de arquivos mesmo quando o espaço livre não é contíguo.
   - Otimizar o uso da memória e gerenciar os buracos que surgem com a criação e exclusão de arquivos.


---

## 📚 Conceitos de Sistemas Operacionais Utilizados 🧠

### 📝 Estruturas de Dados

- **Lista Encadeada**: Utilizada para representar os arquivos e o encadeamento dos blocos.
- **Mapa de Bits (Bitmap)**: Usado para gerenciar os blocos livres e ocupados na memória.

### 🔧 Gerenciamento de Memória

- **Fragmentação de Memória**: Lida com espaços livres não contíguos e otimiza a alocação de novos arquivos.
- **Alocação Dinâmica**: Blocos são alocados e liberados conforme a necessidade.

---

## 🛠️ Funcionalidades Implementadas 🛠️

- **Criação de Arquivos** 📄:
  - O usuário pode criar arquivos com nomes e conteúdos personalizados.
  - O sistema verifica se há memória suficiente e aloca blocos, mesmo que não sejam contíguos.

- **Leitura de Arquivos** 📖:
  - Permite ao usuário ler o conteúdo de arquivos existentes.
  - Percorre os blocos encadeados para reconstruir o conteúdo do arquivo.

- **Exclusão de Arquivos** 🗑️:
  - O usuário pode excluir arquivos, liberando os blocos ocupados para serem reutilizados.
  - Atualiza o mapa de bits para refletir os blocos liberados.

- **Visualização do Disco e Tabela de Arquivos** 🗂️:
  - Exibe o estado atual do disco, mostrando quais blocos estão livres ou ocupados.
  - Mostra a tabela de arquivos com informações como nome, tamanho e endereço inicial.

---

## 💻 Como Executar o Projeto 💡

### Pré-requisitos

- **Python 3.x** instalado.
- Biblioteca **rich** instalada para aprimorar a interface do terminal.

### Instalação da Biblioteca `rich`

No terminal, execute:

```
pip install rich
```
### Execução

No diretório do projeto, execute:
```
python main.py
```

**❕❗❕ Observação: É possível executar o código sem a instalação da biblioteca, mas o código que deverá ser executado é o main_sem_rich.py ❗❕❗**

---

## 🖱️ Como Utilizar 🖱️

1. **Menu Principal**: Ao iniciar o programa, você verá as seguintes opções:

```
[1] Criar Arquivo
[2] Ler Arquivo
[3] Excluir Arquivo
[4] Mostrar Tabela de Arquivos
[5] Mostrar Estado do Disco
[0] Sair
```

2. **Criar Arquivo** 📝:

   - Selecione `[1]` para criar um novo arquivo.
   - Insira o **nome** e o **conteúdo** do arquivo quando solicitado.
   - O sistema alocará os blocos necessários e exibirá uma mensagem de sucesso.

3. **Ler Arquivo** 🔍:

   - Selecione `[2]` para ler um arquivo existente.
   - Insira o **nome** do arquivo que deseja ler.
   - O conteúdo do arquivo será exibido na tela.

4. **Excluir Arquivo** ❌:

   - Selecione `[3]` para excluir um arquivo.
   - Insira o **nome** do arquivo que deseja excluir.
   - O sistema liberará os blocos ocupados e confirmará a exclusão.

5. **Mostrar Tabela de Arquivos** 📋:

   - Selecione `[4]` para visualizar a tabela de arquivos armazenados.

6. **Mostrar Estado do Disco** 💽:

   - Selecione `[5]` para visualizar o estado atual do disco.

7. **Sair** 🏁:

   - Selecione `[0]` para encerrar o programa.

---


## 📜 Licença ⚖️

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---