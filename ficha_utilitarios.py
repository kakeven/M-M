
from poderes import efeitos_poderes_dicionario,pericias_por_habilidade,extras_dict_atualizado,falhas_dict_atualizado

def validar_tudo(nome,categoria):
    return nome in categoria

def listar_atributos(categoria):
    for i,item in enumerate(categoria,start=1):
        print(f"{i} - ",item)

def listar_poderes(categoria):
    for i,item in enumerate(categoria,start=1):
        print(f"{i} - ",item['nome'])

def listar_ficha(categoria,chave1,chave2):
    for i,item in enumerate(categoria,start=1):
        print(f"{item[chave1]} | graduação: {item[chave2]}")

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
            continue

        indice = int(escolha) - 1
        if 0 <= indice < len(lista):
            return lista[indice]
        else:
            print("Número fora do intervalo.")
           
def simplificar_pericia(ficha):   
    nomePericia=escolher_da_lista(ficha.pericias_oficiais)
    if(validar_tudo(nomePericia,ficha.pericias_oficiais)):
        habilidade=ver_pericia(ficha,nomePericia)
        pontosInvestidos = verificar_digito("Digite quantos pontos vai investir na pericia: \n")
        ficha.adicionarPericia(nomePericia=nomePericia,habilidade=habilidade,pontosInvs=pontosInvestidos)
    else:
        print("Pericia invalida!")

def simplificar_habilidade(ficha):              
    nomeHabilidade=escolher_da_lista(ficha.habilidades_oficiais)
    if(validar_tudo(nomeHabilidade,ficha.habilidades_oficiais)):
        pontosInvestidos=verificar_digito("digite quantas graduações vai investir na habilidade: \n")
        ficha.adicionarHabilidades(nomeHabilidade=nomeHabilidade,gra=pontosInvestidos)
    else:
        print("\nHabilidade invalida!")

def simplificar_vantagem(ficha):
    print("Vantagens são normalmente compras únicas,então apenas é necessário 1 ponto, porém algumas podem ter nivel, atente-se!\n")
    nomeVantagem=escolher_da_lista(ficha.vantagens_oficiais)
    if(validar_tudo(nomeVantagem,ficha.vantagens_oficiais)):
        pontosInvestidos=verificar_digito("Digite quantos pontos vai investir: \n")
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
            graduacao = verificar_digito("Graduação: ")
            custo_base=custo
            
        else:
            # Agora coleta os dados do componente
            nomeComponente = input("Nome do componente: ")
            efeito=efeito_escolhido
            graduacao = verificar_digito("Graduação: ")
            custo_base = verificar_digito("Custo base: ")
            
        
            
        
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

def calcular_custosComponente(custo_base,graduacao,mod_g,mod_f):
    custo_total=(custo_base+mod_g) * graduacao + mod_f
    return custo_total

def calcular_custosPoderes(poder):
    custo_total=0

    for componente in poder["componentes"]:
        custo=calcular_custosComponente(custo_base=componente["custo_base"],
        mod_g=componente["mod_por_graduacao"],
        mod_f=componente["mod_fixo"],
        graduacao = componente["graduacao"]
        )
    
        
        componente["custo_total"] = custo
        custo_total += custo
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
    
    #verifica se o valor é uma lista
    if isinstance(extra["valor"],list):
        valor = escolher_da_lista(extra["valor"])   
    else:
        valor = extra["valor"]
    tipo = extra["tipo"]
    
    #incializa o mod, para somar direto e sobreescrever
    mod_g=componente["mod_por_graduacao"]
    mod_f=componente["mod_fixo"]
    
    #verifca e decide o tipo
    if tipo == "por_graduacao":
        mod_g+=valor
        componente["mod_por_graduacao"]=mod_g
    else:
        mod_f+=valor
        componente["mod_fixo"]=mod_f
    
    custoDepois=calcular_custosComponente(custo_base=custobase,graduacao=graduacao,mod_g=mod_g,mod_f=mod_f)
    
    
    resultado= custoDepois - custo_antes
    componente["custo_total"]=custoDepois
    
    ficha.adicionarExtrasComponentes(componente_nome,efeito_extra,valor,tipo)
    ficha.pontosDisponiveis -= resultado
    
def simplificar_extraPoder(ficha):
    
    listar_poderes(ficha.poderes)
    p=escolher_tudo(ficha.poderes)
   
    if "extras" not in p:
        p["extras"] = {}
    #pegar objeto poder
    
   
    #calcular o custo antes do extra
    antigo_custo=sum(componente["custo_total"] for componente in p["componentes"])
    
    extra_poder = ["afeta outros","descritor variavel","efeito alternativo","ligado"]
    
    #mostra e escolhe o efeito
    listar_atributos(extra_poder)
    print("Somente esses efeitos podem ser aplicados a todo o conjunto poder\n")
    efeito_extra = escolher_da_lista(extra_poder)

    #pegar objeto extra
    e = extras_dict_atualizado[efeito_extra]
    
    
    if isinstance (e["valor"],list):
        valor=escolher_da_lista(e["valor"])
    else:
        valor = e["valor"]

    

    tipo=e["tipo"]
    
    for componente in p["componentes"]:
        if tipo == "por_graduacao":
            componente["mod_por_graduacao"] += valor
        else:
            componente["mod_fixo"] += valor


    
    novo_custo= calcular_custosPoderes(p)
    diferenca = novo_custo - antigo_custo
    if ficha.pontosDisponiveis < diferenca and diferenca >0:
        print("Você nao possui pontos suficientes")
        return
    ficha.adicionarExtrasPoderes(p,efeito_extra,valor)
    ficha.pontosDisponiveis -= diferenca

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

        #pegar objeto de componente
        componente = None
        for c in poder["componentes"]:
            if c["nome"] == componente_nome:
                componente = c
                break

        custo_antes = componente["custo_total"]
        custobase= componente["custo_base"]
        graduacao = componente["graduacao"]

        #mostra e escolhe o efeito
        efeito_extra_lista = list(falhas_dict_atualizado)
        
        efeito_extra = escolher_da_lista(efeito_extra_lista)
        falha = falhas_dict_atualizado[efeito_extra]
        valor = falha["valor"]
        if isinstance(valor,list):
            valor= escolher_da_lista(valor)        

        tipo= falha["tipo"]

         #incializa o mod, para somar direto e sobreescrever
        mod_g=componente["mod_por_graduacao"]
        mod_f=componente["mod_fixo"]
        
        #verifca e decide o tipo
        if tipo == "por_graduacao":
            mod_g+=valor
            componente["mod_por_graduacao"]=mod_g
        else:
            mod_f+=valor
            componente["mod_fixo"]=mod_f
            
        
        custoDepois=calcular_custosComponente(custo_base=custobase,graduacao=graduacao,mod_g=mod_g,mod_f=mod_f)
    
        resultado= custoDepois - custo_antes
        componente["custo_total"]=custoDepois
        
        ficha.adicionarFalhasComponentes(componente_nome,efeito_extra,valor,tipo)
        
        #RESULTADO É NEGATIVO, ENT PONTOS - (-RESULTADO) = PONTOS+RESULTADO
        ficha.pontosDisponiveis -= resultado

def simplificar_falhaPoderes(ficha):
    

    listar_poderes(ficha.poderes)
    p=escolher_tudo(ficha.poderes)
    
    if "falhas" not in p:
        p["falhas"] = {}

    #calcular o custo antes do extra
    antigo_custo=sum(componente["custo_total"] for componente in p["componentes"])
    
    falhas_variaveis=["acao aumentada","alcance reduzido","ativacao","efeito colateral","removivel"]

    #mostra e escolhe o efeito
    listar_atributos(falhas_variaveis)
    print("Somente esses efeitos podem ser aplicados a todo o conjunto poder\n")
    efeito_extra = escolher_da_lista(falhas_variaveis)


    if efeito_extra == "removivel":
        intensidade=verificar_digito("Digite a intensidade(1 ou 2): ")
        if intensidade == 1:
            soma = sum(c["custo_total"] for c in p["componentes"])
            desconto= soma //5
            
            ficha.pontosDisponiveis += desconto
            ficha.adicionarFalhasPoderes(p,efeito_extra,intensidade)
            return
        elif intensidade == 2:
            soma = sum(c["custo_total"] for c in p["componentes"])
            desconto= (soma //5) *2
            
            ficha.pontosDisponiveis += desconto
            ficha.adicionarFalhasPoderes(p,efeito_extra,intensidade)
            return


    #pegar objeto extra
    e = falhas_dict_atualizado[efeito_extra]
    
    
    if isinstance (e["valor"],list):
        valor=escolher_da_lista(e["valor"])
    else:
        valor = e["valor"]

    tipo=e["tipo"]
    
    for componente in p["componentes"]:
        if tipo == "por_graduacao":
            componente["mod_por_graduacao"] += valor
        else:
            componente["mod_fixo"] += valor


    
    novo_custo= calcular_custosPoderes(p)
    diferenca = novo_custo - antigo_custo
    if ficha.pontosDisponiveis < diferenca and diferenca >0:
        print("Você nao possui pontos suficientes")
        return
    ficha.adicionarFalhasPoderes(p,efeito_extra,valor)
    ficha.pontosDisponiveis -= diferenca

def verificar_digito(mensagem):
    
    while True:
        variavel= input(mensagem)
        if variavel.isdigit():
            return int(variavel)
       
        print("\nDigite apenas números válidos.")

def mostrar_ficha_atual(ficha):

    print("-----------------FICHA-----------------")
    print(f"Nome do jogador: {ficha.nomeJogador}")
    print(f"Nome do personagem: {ficha.nomePersonagem}")
    print(f"Nivel de poder(NP): {ficha.np} | pontos disponiveis: {ficha.pontosDisponiveis}")
    print("\n")
    print(f"""  HABILIDADES: 
    
        Força: {ficha.habilidades["forca"]}
        Agilidade: {ficha.habilidades["agilidade"]}
        Destreza: {ficha.habilidades["destreza"]}
        Intelecto: {ficha.habilidades["intelecto"]}
        Luta: {ficha.habilidades["luta"]}
        Vigor: {ficha.habilidades["vigor"]}
        Prontidão: {ficha.habilidades["prontidao"]}
        Presença: {ficha.habilidades["presenca"]}
""")
    print("     VANTAGENS: ")
    
    if ficha.vantagens:
       listar_ficha(ficha.vantagens,"nome","graduacao")
         
    else:
        print("Nenhuma vantagem adquirida")


    print("\n   PERICIAS: ")

    if ficha.pericias:
        listar_ficha(ficha.pericias,"nome","graduação") 
    else:
        print("Nenhuma pericia adquirida")

    print("\n   PODERES: ")

    if ficha.poderes:
        for poder in ficha.poderes:
            print(f"\n🧬 Poder: {poder['nome']}")

            if poder.get("falhas"):
                print(f"  Falhas do poder: {poder['falhas']}")

            for componente in poder["componentes"]:
                print(f"""
        ▶ Componente: {componente['nome']}
            Efeito: {componente['efeito']}
            Graduação: {componente['graduacao']}
            Custo total: {componente['custo_total']}
                """)

                if componente["extras"]:
                    print(f"    Extras: {list(componente['extras'].keys())}")

                if componente["falhas"]:
                    print(f"    Falhas: {list(componente['falhas'].keys())}")




    else:
        print("Nenhum poder adquirido")
    
    print("-----------------FICHA-----------------")