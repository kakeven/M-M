
from poderes import *

def validar_tudo(nome,categoria):
    return nome in categoria

def listar_atributos(categoria):
    for i,item in enumerate(categoria,start=1):
        print(f"{i} - ",item)

def listar_poderes(categoria):
    for i,item in enumerate(categoria,start=1):
        print(f"{i} - ",item['nome'])
            
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
    listar_atributos(ficha.pericias_oficiais)             
    nomePericia=input("Nome da pericia: ")
    if(validar_tudo(nomePericia,ficha.pericias_oficiais)):
        habilidade=int(input("Digite o bonus da habilidade correspondente. Ex: forca 4, digite 4: "))
        pontosInvestidos = int(input("Digite quantos pontos vai investir na pericia: \n"))
        ficha.adicionarPericia(nomePericia=nomePericia,habilidade=habilidade,pontosInvs=pontosInvestidos)
    else:
        print("Pericia invalida!")

def simplificar_habilidade(ficha):             
    listar_atributos(ficha.habilidades_oficiais)
    nomeHabilidade=input("Nome da habilidade: ")
    if(validar_tudo(nomeHabilidade,ficha.habilidades_oficiais)):
        pontosInvestidos=int(input("digite quantas graduações vai investir na habilidade: \n"))
        ficha.adicionarHabilidades(nomeHabilidade=nomeHabilidade,gra=pontosInvestidos)
    else:
        print("\nHabilidade invalida!")

def simplificar_vantagem(ficha):
    print("Vantagens são normalmente compras únicas,então apenas é necessário 1 ponto, porém algumas podem ter nivel, atente-se!\n")
    listar_atributos(ficha.vantagens_oficiais)
    nomeVantagem=input("Digite o nome da vantagem: ")
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
            extras, falhas = [], []
        else:
            # Agora coleta os dados do componente
            nomeComponente = input("Nome do componente: ")
            efeito=efeito_escolhido
            graduacao = int(input("Graduação: "))
            custo_base = int(input("Custo base: "))
            escolha_mod = input("Vai ter falhas ou extras? 0(não) / 1(sim): ")
            extras, falhas = [], []
            if escolha_mod == "1":
                falhas_str = input("Digite a lista de falhas (ex: -1,-1 ou []): ").strip("[] ")
                extras_str = input("Digite a lista de extras (ex: +1,+1 ou []): ").strip("[] ")

                if falhas_str:
                    falhas = list(map(int, falhas_str.split(",")))
                if extras_str:
                    extras = list(map(int, extras_str.split(",")))
        
        # Adiciona de fato o componente no poder encontrado
        poder_encontrado["componentes"].append({
            "nome": nomeComponente,
            "efeito": efeito,
            "graduacao": graduacao,
            "custo_base": custo_base,
            "extras": extras,
            "falhas": falhas,
            "custo_total": (custo_base + sum(extras) - sum(falhas)) * graduacao
        })

        ficha.pontosDisponiveis -= (custo_base + sum(extras) - sum(falhas)) * graduacao

        print(f"\nComponente '{nomeComponente}' adicionado ao poder '{poder_encontrado['nome']}'!")
        print(f"Pontos restantes: {ficha.pontosDisponiveis}\n") 