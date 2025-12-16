
from poderes import extras_dict,falhas_dict,efeitos_poderes_dicionario,efeitos_poderes_lista,pericias_por_habilidade

def validar_tudo(nome,categoria):
    return nome in categoria

def listar_atributos(categoria):
    for i,item in enumerate(categoria,start=1):
        print(f"{i} - ",item)

def listar_poderes(categoria):
    for i,item in enumerate(categoria,start=1):
        print(f"{i} - ",item['nome'])
            
def listar_poderes_retornar(categoria):
    nomes = [item["nome"] for item in categoria]
    # for i, nome in enumerate(nomes, start=1):
    #     print(f"{i} - {nome}")
    return nomes


def escolher_tudo(categoria):
    escolha = input("Escolha por NUMERO:")
    # Escolha por número (seguro)
    if escolha.isdigit():
        indice = int(escolha) - 1
        if 0 <= indice < len(categoria):
            escolha_encontrado = categoria[indice]
            
            return escolha_encontrado
        else:
            print("Número inválido!")
    else:
        return   

def escolher_da_lista(lista):
    while True:
        print("\nEscolha um item:")
        for i, item in enumerate(lista):
            print(f"{i+1} - {item}")
        escolha = input("Digite o número: ")

        if not escolha.isdigit():
            print("Entrada inválida.")
            return None

        indice = int(escolha) - 1
        if 0 <= indice < len(lista):
            return lista[indice]
        else:
            print("Número fora do intervalo.")
            return None

def simplificar_pericia(ficha):   
    nomePericia=escolher_da_lista(ficha.pericias_oficiais)
    if(validar_tudo(nomePericia,ficha.pericias_oficiais)):
        habilidade=ver_pericia(ficha,nomePericia)
        pontosInvestidos = int(input("Digite quantos pontos vai investir na pericia: \n"))
        ficha.adicionarPericia(nomePericia=nomePericia,habilidade=habilidade,pontosInvs=pontosInvestidos)
    else:
        print("Pericia invalida!")

def simplificar_habilidade(ficha):             
    
    nomeHabilidade=escolher_da_lista(ficha.habilidades_oficiais)
    if(validar_tudo(nomeHabilidade,ficha.habilidades_oficiais)):
        pontosInvestidos=int(input("digite quantas graduações vai investir na habilidade: \n"))
        ficha.adicionarHabilidades(nomeHabilidade=nomeHabilidade,gra=pontosInvestidos)
    else:
        print("\nHabilidade invalida!")

def simplificar_vantagem(ficha):
    print("Vantagens são normalmente compras únicas,então apenas é necessário 1 ponto, porém algumas podem ter nivel, atente-se!\n")
    nomeVantagem=escolher_da_lista(ficha.vantagens_oficiais)
    if(validar_tudo(nomeVantagem,ficha.vantagens_oficiais)):
        pontosInvestidos=int(input("Digite quantos pontos vai investir: \n"))
        ficha.adicionarVantagem(nomeVantagem=nomeVantagem,graduacao=pontosInvestidos)
    else:
        print("\nVantagem invalida!")

def simplificar_componente(ficha):
    #vericação
        if not ficha.poderes:
            print("Nenhum poder criado. Primeiro adicione um poder (opção 4).")
            return
        #lista
        listar_poderes(ficha.poderes)
        #escolher
        poder_encontrado=escolher_tudo(ficha.poderes)

        # Escolha do efeito a partir da lista
        efeito_escolhido = escolher_da_lista(ficha.poderes_lista)
        if efeito_escolhido is None:
            return
        
        if efeito_escolhido in efeitos_poderes_dicionario:
            dado=efeitos_poderes_dicionario[efeito_escolhido]
            custo = dado["custo"]
        
        if isinstance(custo, (int, float)):
            nomeComponente = input("Nome do componente: ")
            efeito=efeito_escolhido
            graduacao = int(input("Graduação: "))
            custo_base=custo
            
        else:
            # Agora coleta os dados do componente
            nomeComponente = input("Nome do componente: ")
            efeito=efeito_escolhido
            graduacao = int(input("Graduação: "))
            custo_base = int(input("Custo base: "))
            
        
            
        
        # Adiciona de fato o componente no poder encontrado
        poder_encontrado["componentes"].append({
            "nome": nomeComponente,
            "efeito": efeito,
            "graduacao": graduacao,
            "custo_base": custo_base,
            "extras": {},
            "falhas": {},
            "custo_total": custo_base  * graduacao
        })

        ficha.pontosDisponiveis -= custo_base * graduacao

        print(f"\nComponente '{nomeComponente}' adicionado ao poder '{poder_encontrado['nome']}'!")
        print(f"Pontos restantes: {ficha.pontosDisponiveis}\n") 

def ver_pericia(ficha,nomePericia):
    return  ficha.habilidades.get(
        pericias_por_habilidade[nomePericia],0
    )

def simplificar_extraComponente(ficha):
    
    #escolher poder
    listar_poderes(ficha.poderes)
    poder=escolher_tudo(ficha.poderes)
   
   #verificacao
    if not poder["componentes"]:
        print("Esse poder ainda não tem componentes.")
        return

    #mostra e escolhe o componente
    lista_componentes = listar_poderes_retornar(poder["componentes"])
    componente_nome = escolher_da_lista(lista_componentes)
    
    #mostra e escolhe o efeito
    efeito_extra_lista = list(extras_dict.keys())
    efeito_extra = escolher_da_lista(efeito_extra_lista)
    
    if extras_dict[efeito_extra] != 0:
        graduacao = extras_dict[efeito_extra]
    else:
        graduacao=verificar_digito("Digite a graduação: ")


    ficha.pontosDisponiveis -= graduacao
    ficha.adicionarExtrasComponentes(componente_nome,efeito_extra)

def simplificar_extraPoder(ficha):
    ...

def simplificar_falhaComponente(ficha):
    #escolher poder
    listar_poderes(ficha.poderes)
    poder=escolher_tudo(ficha.poderes)
   
   #verificacao
    if not poder["componentes"]:
        print("Esse poder ainda não tem componentes.")
        return

    #mostra e escolhe o componente
    lista_componentes = listar_poderes_retornar(poder["componentes"])
    componente_nome = escolher_da_lista(lista_componentes)
    
    #mostra e escolhe o efeito
    efeito_extra_lista = list(falhas_dict.keys())
    efeito_extra = escolher_da_lista(efeito_extra_lista)
    
    if efeito_extra == "removivel":
        graduacao=verificar_digito("Digite a graduação(-1 ou -2): ")
        if graduacao == -1:
           soma = sum(c["custo_total"] for c in poder["componentes"])
               


    if falhas_dict[efeito_extra] != 0:
        graduacao = falhas_dict[efeito_extra]
    else:
        graduacao=verificar_digito("Digite a graduação: ")


    ficha.pontosDisponiveis -= graduacao
    ficha.adicionarFalhasComponentes(componente_nome,efeito_extra)

def verificar_digito(mensagem):
    
    while True:
        variavel= input(mensagem)
        if variavel.isdigit():
            return int(variavel)
       
        print("\nDigite apenas numeros cara, não é tao dificil")