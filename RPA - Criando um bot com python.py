#RPA - Criando um bot com python

# Observações
## P/ pausar a automacao basta levar a seta do mouse ao canto superior esquerdo da tela e esperar 5 s

# Passo a passo do projeto

# Passo 1 - Entrar no sistema da empresa
    ## Site de testes https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2 - Fazer login
# Passo 3 - Importar base de dados
# Passo 4 - Cadastrar um produto 
# Passo 5 - Repetir isso até terminar a base de dados

# === INÍCIO ===
    # Passo 1
# Instalando biblioteca pyautogui
import pyautogui
import time

# Criando um timer para cada execução do pyautogui 
pyautogui.PAUSE = 1 # 1 segundo de delay para cada ação do pyautogui

# Abrindo o navegador 
pyautogui.press("win") # Clica no botão do windows
pyautogui.write("chrome") # Digita a palavra chrome na pesquisa
pyautogui.press("enter") # Clica na tecla enter para abrir o chrome

# Tempo para carregar a página web
time.sleep(5) # 5 segundos, é executado apenas nessa parte do código

# Digitando o site no navegador
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # Atribuindo variável ao link
pyautogui.write(link) # Digita o site na pesquisa
pyautogui.press("enter") # Aperta a tecla enter

# Tempo para carregar a página web
time.sleep(5) # 5 segundos, é executado apenas nessa parte do código

    # Passo 2
# Fazer Login
pyautogui.click(x=698, y=517) # Clicar no box de preenchimento (ajuda do auxiliar.py)
pyautogui.write("teste@gmail.com") # Digita o email
pyautogui.press("tab") # Aperta tab para passar de campo de preenchimento
pyautogui.write("sua senha") # Digita sua senha
pyautogui.press("tab") # Aperta tab para passar para o botão de logar
pyautogui.press("enter") # Aperta a tecla enter para logar

    # Passo 3
# Importar a base de dados - instalar pandas
#pip install pandas
import pandas

tabela = pandas.read_csv("produtos.csv")
print (tabela)

    # Passo 4 e 5
for linha in tabela.index:
    # Cadastrar um produto
    pyautogui.click(x=719, y=368) # Clica no primeiro box de preenchimento do formulário
    # Codigo
    codigo = tabela.loc[linha, "codigo"] # Comando loc para pegar informação na tabela
    pyautogui.write(codigo) # Digita o codigo do produto
    pyautogui.press("tab")
    # Marca
    pyautogui.write(tabela.loc[linha, "marca"]) # Digita a marca do produto
    pyautogui.press("tab")
    # Tipo
    pyautogui.write(tabela.loc[linha, "tipo"]) # Digita o tipo do produto
    pyautogui.press("tab")
    # Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"])) # Digita a categoria do produto 
    pyautogui.press("tab")
    # Preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) # Digita o preco_unitario do produto
    pyautogui.press("tab")
    # Custo
    pyautogui.write(str(tabela.loc[linha, "custo"])) # Digita o custo do produto
    pyautogui.press("tab")
    # Obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # Verifica se o obs é NaN, só digita se não for
        pyautogui.write(obs) # Digita a obs do produto
    # Enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter") # Enviar o produto
    # Subir a página pro topo
    pyautogui.scroll(5000) # número positivo vai pra cima e número negativo para baixo
