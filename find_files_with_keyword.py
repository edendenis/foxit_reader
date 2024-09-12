# -*- coding: utf-8 -*-
import os

def find_files_with_keyword(directory, keyword):
    """
    Percorre os arquivos .py de um diretório e retorna uma lista dos arquivos que contêm a palavra-chave especificada.

    :param directory: Caminho do diretório a ser percorrido.
    :type directory: str
    :param keyword: Palavra-chave a ser procurada nos arquivos.
    :type keyword: str
    :return: Lista de caminhos dos arquivos que contêm a palavra-chave.
    :rtype: list
    """
    matching_files = []
    
    # Percorre todos os arquivos do diretório e subdiretórios
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                # Abre e lê o conteúdo do arquivo
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Verifica se a palavra-chave está no conteúdo do arquivo
                        if keyword in content:
                            matching_files.append(file_path)
                except Exception as e:
                    print(f"Erro ao ler o arquivo {file_path}: {e}")
    
    return matching_files

# Diretório a partir do qual começar a busca (raiz do projeto)
project_root_directory = os.path.dirname(os.path.abspath(__file__))

# Pergunta a palavra-chave ao usuário
keyword_to_find = input('Please enter the keyword to search for: ')

# Chama a função e exibe os arquivos encontrados
files_found = find_files_with_keyword(project_root_directory, keyword_to_find)
print(f'Files containing the word "{keyword_to_find}":')
for file in files_found:
    # Imprime o caminho do arquivo em formato de link clicável
    print(f'file://{file}')

# Referências

# [1] OPENAI.
# Encontrar arquivos com palavra.
# Disponível em: <https://chatgpt.com/c/3e5f15f5-ee76-43db-b668-c9a678fe8009>.
# Acessado em: 08/08/2024 09:54.  
