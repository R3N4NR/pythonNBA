import os.path            # importa pacote com rotinas relacionadas a operações do so

# declara vetores globais
times= [];
time = [];
conferencia = [];
mascotes = [];


def titulo(texto, simbolo="-"):
    print()
    print(texto)
    print(simbolo*23)


def incluir():
    titulo("Inclusão de Times")
    time = input("Time: ")

    sel = int(input("Conferência da equipe (1. Leste || 2. Oeste):"))
    if sel == 1:
        
        times.append(time + ';Leste')
        print(f"{time} inserido na conferencia LESTE ")
    else:

        times.append(time + ';Oeste')
        print(f"{time} inserido na conferencia OESTE ")



def listar():
    titulo(" "*20 + "Lista de Times" )
    print("ID Equipe                   Conferência \n")
    
    # for i, (confLeste, confOeste) in enumerate(zip(conferenciaLeste, conferenciaOeste),start=1):
        
    #     print(f"{confLeste:<34}  {confOeste:<35}")
    
        
    c=0;
    if times:
       for i in times:
        c+=1;
        separadorL = i.split(";");
        time = separadorL[0];
        conferencia = separadorL[1];
        print(f"{c}.{time:<30}{conferencia:<30} ")
    else:
        print("Não há equipes registradas")
        return
    # for linhaS in linhasS:
    #        separador = linhaS.split(";")
    #        time.append(separador[0]);
           #conferencia.append(separador[1])
        #    print(f"{time}")

def pesquisar():
    titulo(" "*20 + "Pesquisar Times\n" )
    keyword = input("Pesquisa por nome ou conferencia: ")
    print("\nTime                                 Conferência\n")
    print("="*50)
    contador = 0;
    for i in times:
        separadorP = i.split(";")
        time = separadorP[0];
        conferencia = separadorP[1];
        if keyword.upper() in i.upper():    
                print(f"{time:<37}{conferencia:<38}")
                contador +=1
    
    if contador == 0:
                print(f"A equipe {keyword} não existe! ")
                print("="*50)


def excluir():
    listar()
    titulo("Excluir time")
    exc = int(input("ID do time (0 para sair): "))
    if exc == 0:
        return
    controla = exc - 1
    mensagem = times.pop(controla)
    
    print(f"Sucesso !O time {controla+1} foi excluído !")

def alterar():
    listar()
    titulo("Editar dados")
    alt = int(input("ID da equipe (0, para sair): "))
    if alt == 0:
        return
    nome_equipe = times[alt-1].split(";")
    novo_nome = input(f"A equipe {nome_equipe[0]} está registrada na conferência {nome_equipe[1]}\nO novo nome será :")
    sel = int(input("Conferência da equipe (1. Leste || 2. Oeste):"))
    if sel == 1:
        times[alt -1]= novo_nome + ';Leste'
        print(f"{novo_nome} alterado na conferencia LESTE ")
    if sel == 2:
        times[alt -1]= novo_nome + ';Oeste'
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

# Programa Principal
while True:
    titulo("Cadastro de Times", "=")
    print("1. Incluir Time")
    print("2. Listagem de Times")
    print("3. Pesquisar")
    print("4. Excluir")
    print("5. Editar Times")
    print("6. Resumo")
    print("7. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
 
    elif opcao == 3:
        pesquisar()
        
    elif opcao == 4:
         excluir()
       
    elif opcao == 5:
        alterar()
        
    elif opcao == 6:
        resumo()
        
    else:
        break

# executa ao finalizar o programa (salva os dados)
salvar()
