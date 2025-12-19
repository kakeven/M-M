
from poderes import extras_dict,falhas_dict,efeitos_poderes_dicionario,pericias_por_habilidade,extras_dict_atualizado,extra_hibrido

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
            "mod_por_graduacao": 0,
            "mod_fixo": 0,
            "custo_total": custo_base  * graduacao
        })

        ficha.pontosDisponiveis -= custo_base * graduacao

        print(f"\nComponente '{nomeComponente}' adicionado ao poder '{poder_encontrado['nome']}'!")
        print(f"Pontos restantes: {ficha.pontosDisponiveis}\n") 

def ver_pericia(ficha,nomePericia):
    return  ficha.habilidades.get(
        pericias_por_habilidade[nomePericia],0
    )

def calcular_custosComponente(tipo,valor_tipo,custo_base,graduacao):
    if tipo == "por_graduacao":
        custo_base += valor_tipo
        custo_total = custo_base *graduacao
        return custo_total
    
    elif tipo=="fixo":
        custo_total = valor_tipo + custo_base*graduacao
        return custo_total






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
    

    # pegar o OBJETO do componente
    componente = None
    for c in poder["componentes"]:
        if c["nome"] == componente_nome:
            componente = c
            break

    custobase= componente["custo_base"]
    graduacao = componente["graduacao"]
    
    
    #mostra e escolhe o efeito
    efeito_extra_lista = list(extras_dict_atualizado.keys())
    efeito_extra = escolher_da_lista(efeito_extra_lista)
    
    #pegando o objeto do extra
    extra = extras_dict_atualizado[efeito_extra]
    custo_antes = componente["custo_total"]
    
    if isinstance(extra["valor"],list):
        valor = escolher_da_lista(extra["valor"])   
    else:
        valor = extra["valor"]
    tipo = extra["tipo"]
    
    if tipo == "por_graduacao":
        componente["mod_por_graduacao"]+=valor
    else:
        componente["mod_fixo"]+=valor

    custoDepois=calcular_custosComponente(tipo=tipo,valor_tipo=valor,custo_base=custobase,graduacao=graduacao)
    resultado=custoDepois-custo_antes
    
    componente["custo_total"]+= resultado
    
    ficha.adicionarExtrasComponentes(componente_nome,efeito_extra,valor,tipo)
    ficha.pontosDisponiveis -= resultado
    

# def simplificar_extraPoder(ficha):
#     listar_poderes(ficha.poderes)
#     nomePoder=escolher_tudo(ficha.poderes)
   
#     for poder in ficha.poderes:
#         if nomePoder == poder:
#             p = poder
   
#     #mostra e escolhe o efeito
#     efeito_extra_lista = listar_poderes(extra_hibrido)
#     efeito_extra = escolher_da_lista(efeito_extra_lista)

#     for extra in extras_dict_atualizado:
#         if efeito_extra == extra['nome']:
#             e = extra
    

# def simplificar_falhaComponente(ficha):
#     #escolher poder
#     listar_poderes(ficha.poderes)
#     poder=escolher_tudo(ficha.poderes)
   
#    #verificacao
#     if not poder["componentes"]:
#         print("Esse poder ainda não tem componentes.")
#         return

#     #mostra e escolhe o componente
#     lista_componentes = listar_poderes_retornar(poder["componentes"])
#     componente_nome = escolher_da_lista(lista_componentes)
    
#     #mostra e escolhe o efeito
#     efeito_extra_lista = list(falhas_dict.keys())
#     efeito_extra = escolher_da_lista(efeito_extra_lista)
    
#     if falhas_dict[efeito_extra] != 0:
#         graduacao = falhas_dict[efeito_extra]
#     else:
#         graduacao=verificar_digito("Digite a graduação: ")


#     ficha.pontosDisponiveis -= graduacao
#     ficha.adicionarFalhasComponentes(componente_nome,efeito_extra)

# def simplificar_falhaPoderes(ficha):
#     listar_poderes(ficha.poderes)
#     nomePoder=escolher_tudo(ficha.poderes)
   
   
#     #mostra e escolhe o efeito
#     efeito_extra_lista = list(falhas_dict.keys())
#     efeito_extra = escolher_da_lista(efeito_extra_lista)
    
#     if efeito_extra == "removivel":
#             intensidade=verificar_digito("Digite a intensidade(1 ou 2): ")
#             if intensidade == 1:
#                 soma = sum(c["custo_total"] for c in nomePoder["componentes"])
#                 desconto= soma //5
                
#                 ficha.pontosDisponiveis += desconto
#                 ficha.adicionarFalhasPoderes(nomePoder["nome"],efeito_extra,intensidade)
#             elif intensidade == 2:
#                 soma = sum(c["custo_total"] for c in nomePoder["componentes"])
#                 desconto= (soma //5) *2
                
#                 ficha.pontosDisponiveis += desconto
#                 ficha.adicionarFalhasPoderes(nomePoder["nome"],efeito_extra,intensidade)

#     falhas_variaveis=["acao aumentada","alcance reduzido","ativacao","efeito colateral"]

#     if efeito_extra in falhas_variaveis:
#         graduacao=verificar_digito("Digite a graduação: ")
#         custo_base = verificar_digito("Digite o custo base")
#         ficha.pontosDisponiveis += (graduacao*custo_base)
#         ficha.adicionarFalhasPoderes(nomePoder["nome"],efeito_extra,graduacao)
#     else:
#         graduacao=verificar_digito("Digite a graduação: ")
#         ficha.pontosDisponiveis += graduacao
#         ficha.adicionarFalhasPoderes(nomePoder["nome"],efeito_extra,graduacao)

def verificar_digito(mensagem):
    
    while True:
        variavel= input(mensagem)
        if variavel.isdigit():
            return int(variavel)
       
        print("\nDigite apenas numeros cara, não é tao dificil")