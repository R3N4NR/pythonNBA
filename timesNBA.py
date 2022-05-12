 # importa pacote com rotinas relacionadas a operações do so
import os.path           

# declara vetores globais
times= [];
time = [];
conferencia = [];
mascotes = [];


def titulo(texto, simbolo="-"):
    print()
    print(texto)
    print(simbolo*23)


def incluirTimes():
    titulo("Inclusão de Times")
    time = input("Time: ")
# variável alterada de sel para selecionaConferencia
    selecionaConferencia = int(input("Conferência da equipe (1. Leste || 2. Oeste):"))
    if selecionaConferencia == 1:
        
        times.append(time + ';Leste')
        print(f"{time} inserido na conferencia LESTE ")
    else:

        times.append(time + ';Oeste')
        print(f"{time} inserido na conferencia OESTE ")

def listarTimes():
    titulo(" "*20 + "Lista de Times" )
    print("ID Equipe                   Conferência \n")
   #desta linha até a linha 38 haviam comentários inutilizados 
   # na linha 36 havia a variável c e foi alterada para flag    
    flag=0; 
    if times:
       for i in times:
        flag+=1;
        #a variável separador possuía o nome de separadorL
        separador = i.split(";");
        time = separador[0];
        conferencia = separador[1];
        print(f"{c}.{time:<30}{conferencia:<30} ")
    else:
        print("Não há equipes registradas")
        return
    #das linhas 50 até 54 haviam comentários inutilizados
def pesquisarTimes():
    titulo(" "*20 + "PesquisarTimes Times\n" )
    keyword = input("Pesquisa por nome ou conferencia: ")
    print("\nTime                                 Conferência\n")
    print("="*50)
    flag = 0;
    for i in times:
        separador = i.split(";")
        #a variavel separador possuia o nome de separadorP
        time = separador[0];
        conferencia = separador[1];
        if keyword.upper() in i.upper():    
                print(f"{time:<37}{conferencia:<38}")
                flag +=1
    
    if flag == 0:
                print(f"A equipe {keyword} não encontrado ;) ")
                print("="*50)

def excluirTimes():
    listarTimes()
    titulo("ExcluirTimes time")

    #a variavel idExclusao era chamada de exc
    idExclusao = int(input("ID do time (0 para sair): "))
    if idExclusao == 0:
        return
    controla = idExclusao - 1
    mensagem = times.pop(controla)
    
    print(f"Sucesso !O time {controla+1} foi excluído !")

def alterarTimes():

    listarTimes()
    
    titulo("Editar dados")

    #a variavel id Alteracao era chamada de alt
    idAlteracao = int(input("ID da equipe (0, para sair): "))
    
    if idAlteracao == 0:
        return
        #as variaveis nomeEquipe e novoNome eram nomeadas como nome_equipe e novo_nome
    nomeEquipe = times[idAlteracao-1].split(";")
    novoNome = input(f"A equipe {nomeEquipe[0]} está registrada na conferência {nomeEquipe[1]}\nO novo nome será :")
   
    selecionaConferencia = int(input("Conferência da equipe (1. Leste || 2. Oeste):"))

    if selecionaConferencia == 1:
        times[alt -1]= novoNome + ';Leste'
        print(f"{novo_nome} alterado na conferencia LESTE ")

    if selecionaConferencia == 2:
        times[alt -1]= novoNome + ';Oeste'
        print(f"{novo_nome} alterado na conferencia OESTE ")

    print("Alterações realizadas com sucesso !! ")

def resumo():
    titulo("Resumo ds Equipes")
    num = len(times)
    l =0;
    o =0;
    for parte in times:
        separador = parte.split(";")
        if separador[1].upper() == 'Leste'.upper():
            l+=1

        elif separador[1].upper() == 'Oeste'.upper():
            o +=1
    print(f"Total de equipes: {num}")
    print(f"Nº de equipes na conferência Leste: {l}")
    print(f"Nº de equipes na conferência Oeste: {o}")
    
def salvar():
    # abre o arquivo produtos.txt, no modo "w", que é a criação do arquivo
    with open("times.txt", "w") as arq:
        for time in times:
            arq.write(f"{time}\n")

def carregar_dados():
    # abre o arquivo para leitura (r: read)
    
    with open("times.txt", "r") as arq:
         linhas = arq.read().splitlines()
       
         for linha in linhas:
            partes = linha.split(";")
            times.append(linha)
# no início do programa carrega os dados
if os.path.exists("times.txt"):
    carregar_dados()
#na linha 143 havia um comentário indicando a função while como "programa principal"
while True:
    titulo("Cadastro de Times", "=")
    print("1. IncluirTimes Time")
    print("2. Listagem de Times")
    print("3. Pesquisar Times")
    print("4. Excluir Times")
    print("5. Editar Times")
    print("6. Resumo")
    print("7. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        incluirTimes()
    elif opcao == 2:
        listarTimes()
 
    elif opcao == 3:
        pesquisarTimes()
        
    elif opcao == 4:
         excluirTimes()
       
    elif opcao == 5:
        alterarTimes()
        
    elif opcao == 6:
        resumo()
        
    else:
        break

# executa ao finalizar o programa (salva os dados)
salvar()
