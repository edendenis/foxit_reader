# -*- coding: utf-8 -*-

import os
import shutil
from datetime import datetime

def should_process_directory(dirpath):
    """
    Verifica se o diretório deve ser processado, ignorando diretórios ocultos e .git.
    
    :param dirpath: Caminho do diretório a ser verificado
    :return: True se o diretório deve ser processado, False caso contrário
    """
    # Ignorar diretórios ocultos e .git
    return not (os.path.basename(dirpath).startswith('.') or '.git' in dirpath)

def contains_readme_or_git(dirpath):
    """
    Verifica se o diretório contém um arquivo README ou um diretório .git.
    
    :param dirpath: Caminho do diretório a ser verificado
    :return: True se o diretório contém README ou .git, False caso contrário
    """
    for item in os.listdir(dirpath):
        if item.lower().startswith('readme') or item == '.git':
            return True
    return False

def copy_files_to_non_empty_dir(template_dir, source_files, target_roots):
    """
    Copia arquivos especificados para subpastas dos diretórios alvo que possuem pelo menos um arquivo README ou um diretório .git.
    Adiciona a data de modificação da pasta que está recebendo os arquivos ao arquivo CHANGES.txt se ele não existir.
    Exclui arquivos copiados para subsubpastas.
    
    :param template_dir: Diretório que contém os arquivos e pastas a serem copiados
    :param source_files: Lista de arquivos e/ou pastas para copiar
    :param target_roots: Lista de diretórios raiz onde as cópias serão feitas
    """
    for target_root in target_roots:
        program_dirs = []
        for dirpath, dirnames, filenames in os.walk(target_root):
            if should_process_directory(dirpath):
                if contains_readme_or_git(dirpath):
                    print(f"\nProcessing folder: {dirpath}\n")
                    program_dirs.append(dirpath)
                    for item in source_files:
                        item_path = os.path.join(template_dir, item)
                        target_item_path = os.path.join(dirpath, os.path.basename(item))
                        
                        if os.path.isfile(item_path):
                            # Sobrescrever apenas arquivos de configuração
                            if os.path.basename(item_path) in ['.gitignore', '.gitattributes']:
                                shutil.copy(item_path, dirpath)
                                print(f"File {item} copied to {dirpath}")
                            # Não sobrescrever outros arquivos se já existirem
                            elif not os.path.exists(target_item_path):
                                shutil.copy(item_path, dirpath)
                                print(f"File {item} copied to {dirpath}")
                        elif os.path.isdir(item_path):
                            # Copiar pastas somente se não existirem
                            if not os.path.exists(target_item_path):
                                shutil.copytree(item_path, target_item_path, dirs_exist_ok=True)
                                print(f"Folder {item} copied to {dirpath}")
                    update_changes_file_if_not_exists(dirpath)

        # Remover arquivos copiados erroneamente para subpastas
        for dirpath, dirnames, filenames in os.walk(target_root):
            if dirpath not in program_dirs and should_process_directory(dirpath):
                for item in source_files:
                    item_name = os.path.basename(item)
                    target_item_path = os.path.join(dirpath, item_name)
                    if os.path.isfile(target_item_path) and not (os.path.basename(target_item_path) in ['.gitignore', '.gitattributes']):
                        os.remove(target_item_path)
                        print(f"Removed file {target_item_path}")
                    elif os.path.isdir(target_item_path):
                        shutil.rmtree(target_item_path)
                        print(f"Removed folder {target_item_path}")

def update_changes_file_if_not_exists(dirpath):
    """
    Cria o arquivo CHANGES.txt com a data de modificação do diretório se ele não existir.
    
    :param dirpath: Diretório cujo arquivo CHANGES.txt será criado
    """
    changes_file_path = os.path.join(dirpath, 'CHANGES.txt')
    
    if not os.path.exists(changes_file_path):
        mod_time = os.path.getmtime(dirpath)
        mod_date = datetime.fromtimestamp(mod_time).strftime('%d/%m/%Y')
        
        with open(changes_file_path, 'w', encoding='utf-8') as f:
            f.write("Histórico de Revisões/Versões\n")
            f.write("==============================\n\n")
            f.write(f"**Revisão 0** - {mod_date}\n")
            f.write(f"- Pasta modificada em {mod_date}.\n")
    else:
        print(f"CHANGES.txt already exists in {dirpath}, not modified.")

# Exemplo de uso
template_dir = 'TEMPLATE'  # Diretório que contém os arquivos e pastas a serem copiados
source_files = ['figures',
                '.gitattributes',
                '.gitignore',
                'CHANGES.txt',
                'copy_files_to_non_empty_dirs.py',
                'convert_md_to_ipynb_and_py.py',
                'convert_ipynb_to_md_and_py.py',
                'LICENSE.txt']  # Lista de pastas e arquivos para copiar
target_roots = ['android', 'debian', 'mac_os', 'ubuntu']  # Lista de diretórios raiz onde as cópias serão feitas

copy_files_to_non_empty_dir(template_dir, source_files, target_roots)

# Referências

# OPENAI.
# Python copy files recursive.
# Disponível em: <https://chatgpt.com/c/87b08629-4a93-49a4-8d94-4048ace8697d>.
# Acessado em: 12/06/2024 09:48.
