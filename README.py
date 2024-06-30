#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `Foxit Reader (Wine)` no terminal no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `Foxit Reader (Wine)` no terminal no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to configure/install/use the `Foxit Reader (Wine)` on `Linux Ubuntu`._

# ## Descrição
# 
# ### `Foxit Reader`
# 
# O `Foxit Reader` é um software de visualização de PDF que oferece uma variedade de funcionalidades além da simples leitura de documentos PDF. Ele permite que os usuários editem texto, insiram anotações, assinem digitalmente, preencham formulários e realizem outras ações em arquivos PDF. Comparado a outros leitores de PDF, como o Adobe Acrobat Reader, o Foxit Reader é conhecido por ser mais leve e rápido, tornando-o uma escolha popular para quem busca eficiência e recursos robustos em um leitor de PDF.

# ## 1. Configurar/Instalar/Usar o `Foxit Reader (Wine)` no `Linux Ubuntu` (caso ainda não esteja instalado) [1]
# 
# Para configurar/instalar/usar o `Foxit Reader` via `Flatpak` no `Linux Ubuntu`, siga os passos abaixo::
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. **Instale o `flatpak`:** com o comando: `sudo apt install flatpak -y`
# 
# 4. **Ativar o UFW:** Para ativar o UFW, execute o comando: `sudo apt install gnome-software-plugin-flatpak -y`
# 
# 5. **Verificar o status do UFW:** Você pode verificar o status do UFW a qualquer momento usando: `flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo`
# 
# 6. **Instale o `bottles`:** com o comando: `flatpak install flathub com.usebottles.bottles -y`
# 
# 7. Para abrir o aplicativo Bottles pelo terminal no Linux, execute o comando: `flatpak run com.usebottles.bottles`

# 8. Clicar em `avançar`

# 9. Clicar em `avançar`:
# 

# 10. Clicar em `Continue`:
# 

# 11. Aguardar até finalizar, ou seja, até aparecer a mensagem `All Ready`:
# 

# 12. Clicar em `Bottles`:
# 

# 13. Clicar em `Create New Bottle...`
# 

# 14. Clicar no campo `Name`:
# 

# 15. Definir um nome para o `Bottle`: (Sugestão) `foxit_pdf_reader`
# 

# 16. Clicar em `create`
# 

# 17. Aguardar a criação do `Bottle`
# 

# 18. Clicar em `Close`
# 

# 19. Clicar em `Run executable in foxit_pdf_reader`
# 

# 20. Selecionar o arquivo executável `FoxitPDFReader20232_enu_Setup_Prom.exe`
# 

# 21. Clicar em `Run`
# 

# 22. Seguir com as instruções do arquivo de instalação executável`.exe`
# 

# Aqui estão os comandos correspondentes para cada etapa:
# 
# ## 1.1 Comentários sobre os comandos
# 
# - **`Ctrl + Alt + T`:** Este atalho de teclado abre um novo terminal no `Ubuntu` e em outros sistemas que utilizam o ambiente de desktop GNOME.
# 
# - **`sudo apt update -y`:** Este comando atualiza a lista de pacotes disponíveis para instalação. O `-y` é uma flag que permite que todas as perguntas sejam automaticamente respondidas com 'sim'.
# 
# - **`sudo apt upgrade -y`:** Este comando atualiza os pacotes já instalados para as suas versões mais recentes, com base na última vez que você executou sudo apt update. O `-y` serve para o mesmo propósito que no comando anterior.
# 
# - **`sudo apt install flatpak -y`:** Este comando instala o pacote `Flatpak`, que é uma ferramenta para gerenciar e instalar aplicativos em formato `Flatpak`.
# 
# - **`sudo apt install gnome-software-plugin-flatpak -y`:** Este comando instala um plugin para o GNOME Software, permitindo que ele gerencie pacotes `Flatpak`. Note que este comando não tem relação com o UFW.
# 
# - **`flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo`:** Este comando adiciona o repositório Flathub ao `Flatpak`, caso ele ainda não esteja adicionado. O Flathub é um repositório de pacotes `Flatpak`.
# 
# - **`flatpak install flathub com.usebottles.bottles -y`:** Este comando instala o aplicativo Bottles do repositório Flathub. Novamente, o `-y` permite que todas as perguntas sejam automaticamente respondidas com 'sim'.
# 
# - **`flatpak run com.usebottles.bottles`:** Este comando executa o aplicativo Bottles instalado via `Flatpak`.
# 

# ## 2.Criar um atalho para o aplicativo [2]
# 
# Para criar um atalho para o `Foxit Reader` instalado via `Bottles/Wine`, você pode criar um arquivo `.desktop` manualmente. Este arquivo será responsável por iniciar o `Foxit Reader` com os parâmetros apropriados. Aqui estão os passos para fazê-lo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# 3. A versão `flatpak` precisa de permissão especial para gerar entradas na área de trabalho. Para conseguir isso, feche o Bottles e, então digite: `flatpak override com.usebottles.bottles --user --filesystem=xdg-data/applications`
# 

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `Foxit Reader (Wine)` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Instalação do bottle no ubuntu.*** Disponível em: <https://chat.openai.com/c/92444ccc-f995-4e9c-8f03-678931882241> (texto adaptado). Acessado em: 01/11/2023 19:17.
# 
# [2] BOTTLES. ***Programs.*** Disponível em: <https://docs.usebottles.com/bottles/programs#flatpak>. Acessado em: 06/05/2023 16:22.
# 
