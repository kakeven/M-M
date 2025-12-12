import json

class Ficha:
    def __init__(self,np,nomeJogador,nomePersonagem):
        
        self.np = np
        pontos_por_np ={
            1: 15, 2: 30, 3: 45, 4: 60, 5: 75,
            6: 90, 7: 105, 8: 120, 9: 135, 10: 150,
            11: 165, 12: 180,13:195,14:210,15:225
        }
        self.total = pontos_por_np[np]         
        self.pontosDisponiveis = self.total
        self.nomeJogador=nomeJogador
        self.nomePersonagem=nomePersonagem

        self.poderes=[]
        self.habilidades=[]
        self.pericias=[]
        self.vantagens=[]

        self.habilidades_oficiais = [
        "forca", "agilidade", "presenca", "vigor",
        "intelecto", "luta", "prontidao","destreza"
        ]

        self.pericias_oficiais = [
            "acrobacia", "atletismo", "investigacao", "percepcao",
            "enganacao", "furtividade", "tecnologia", "intuicao",
            "pilotagem", "veiculos", "medicina", "diplomacia"
        ]

        self.vantagens_oficiais = [
            "acao em movimento",
            "agarrar aprimorado",
            "agarrar preciso",
            "agarrar rapido",
            "ambiente favorito",
            "arma improvisada",
            "armacao",
            "artifice",
            "assustar",
            "ataque acurado",
            "ataque a distancia",
            "ataque corpo a corpo",
            "ataque defensivo",
            "ataque domino",
            "ataque imprudente",
            "ataque poderoso",
            "ataque preciso",
            "atraente",
            "avaliacao",
            "bem informado",
            "bem relacionado",
            "beneficio",
            "capanga",
            "contatos",
            "critico aprimorado",
            "de pe",
            "defesa aprimorada",
            "derrubar aprimorado",
            "desarmar aprimorado",
            "destemido",
            "duro de matar",
            "empatia com animais",
            "equipamento",
            "esconder se a plenas vista",
            "esforco extraordinario",
            "esforco supremo",
            "esquiva fabulosa",
            "estrangular",
            "evasao",
            "fascinar",
            "faz tudo",
            "ferramentas aprimoradas",
            "finta agil",
            "idiomas",
            "imobilizar aprimorado",
            "iniciativa aprimorada",
            "inimigo favorito",
            "inspirar",
            "interpor se",
            "inventor",
            "lideranca",
            "luta no chao",
            "maestria em arremesso",
            "maestria em pericia",
            "memoria eidetica",
            "mira aprimorada",
            "parceiro",
            "prender arma",
            "quebrar aprimorado",
            "quebrar arma",
            "rastrear",
            "redirecionar",
            "ritualista",
            "rolamento defensivo",
            "saque rapido",
            "segunda chance",
            "sorte",
            "sorte de principiante",
            "tolerancia maior",
            "tomar a iniciativa",
            "tontear",
            "trabalho em equipe",
            "transe",
            "zombar"
        ]

    def validar_tudo(self,nome,categoria):
        return nome in categoria

    def adicionarVantagem(self,nomeVantagem,graduacao):        
        custo_graduacao = 1
        custo_total = graduacao * custo_graduacao
        
        if self.pontosDisponiveis<custo_total:
            print(f"Excedeu os pontos, você tem {self.pontosDisponiveis} e o custo é :{custo_total}")
            return
        
        vantagem={
            "nome":nomeVantagem,
            "graduacao":graduacao,
            "pontos gastos": custo_total
        }
        self.pontosDisponiveis -= custo_total
        self.vantagens.append(vantagem)
        print(f"pontos disponiveis: {self.pontosDisponiveis}")

    def adicionarComponente(self, nomeComponente, efeito, graduacao, custo_base, extras=None, falhas=None):
        # segurança contra None
        extras = extras or []
        falhas = falhas or []

        # calcula modificadores
        mod_extras = sum(extras)      # ex: [+1, +1]
        mod_falhas = sum(falhas)      # ex: [-1]

        # custo por graduação já modificado
        custo_grad_final = custo_base + mod_extras - mod_falhas

        if custo_grad_final < 1:
            print("O custo final por graduação não pode ser menor que 1.")
            return

        custo_total = graduacao * custo_grad_final

        if custo_total > self.pontosDisponiveis:
            print(f"Custo excedido. Você tem {self.pontosDisponiveis} pontos.")
            return

        # garante que existe um poder criado
        if not self.poderes:
            print("Nenhum poder criado. Use adicionarPoder primeiro.")
            return

        componente = {
            "nome": nomeComponente,
            "efeito": efeito,
            "graduacao": graduacao,
            "custo_base": custo_base,
            "extras": extras,
            "falhas": falhas,
            "custo_total": custo_total
        }

        self.poderes[-1]["componentes"].append(componente)
        self.pontosDisponiveis -= custo_total

        print(f"Componente {nomeComponente} adicionado!")
        print(f"Graduação: {graduacao}, Custo total: {custo_total}")
        
    def adicionarPoder(self,nomePoder):
        poder = {
            "nome":nomePoder,
            "componentes": []
        }
        self.poderes.append(poder)
        print("poder adicionado")

    def adicionarHabilidades(self,nomeHabilidade,gra):
        custo_graduacao = 2
        custo_total = custo_graduacao * gra
        
        #vericação para nao ter duplicata
        for h in self.habilidades:
            if h["nome"] == nomeHabilidade:
                print("Essa habilidade já foi adicionada.")
                return
        
        if custo_total> self.pontosDisponiveis:
            print(f"Pontos excedentes, você possui: {self.pontosDisponiveis} e quer gastar:{custo_total}")
            return
        else:
            self.pontosDisponiveis -= custo_total
            habilidade = {
                "nome":nomeHabilidade,
                "pontosGastos":custo_total,
                "habilidade": gra
            }
            self.habilidades.append(habilidade)
            print(f"Você possui: {self.pontosDisponiveis}")

    def salvar(self, arquivo="ficha.json"):
        dados = {
            "np": self.np,
            "nomeJogador": self.nomeJogador,
            "nomePersonagem": self.nomePersonagem,
            "pontosDisponiveis": self.pontosDisponiveis,
            "total": self.total,
            "poderes": self.poderes,
            "habilidades": self.habilidades,
            "pericias": self.pericias,
            "vantagens": self.vantagens
        }
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print("Ficha salva!")


    @staticmethod
    def carregar_ficha(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        ficha = Ficha(nomeJogador=dados["nomeJogador"],np=dados["np"],nomePersonagem=dados["nomePersonagem"])  # cria ficha vazia

        # joga tudo do JSON dentro da ficha
        for chave, valor in dados.items():
            setattr(ficha, chave, valor)

        return ficha

    def adicionarPericia(self,nomePericia,habilidade,pontosInvs):
        grad=2
        maxgrad= self.np + 10
        graduacoes = pontosInvs*grad
        bonus = graduacoes+habilidade
        for p in self.pericias:
            if p["nome"] == nomePericia:
                print("Essa perícia já foi adicionada.")
                return

        if maxgrad<graduacoes:
            print(f"A quantidade excedeu os limites de graduação, esse é seu limite:{maxgrad}")
            return
        if self.pontosDisponiveis<pontosInvs:
            print(f"Excedeu o numero de pontos, você possui{self.pontosDisponiveis} e quer gastar:{pontosInvs}")
            return
        
        pericia = {
            "nome":nomePericia,
            "graduação":graduacoes,
            "bonus":bonus,
            "custo":pontosInvs
        }
        self.pontosDisponiveis -= pontosInvs
        self.pericias.append(pericia)
        print(f"Perícia {nomePericia} adicionada!")
        print(f"Graduações: {graduacoes}, Bônus total: {bonus}, Custo: {pontosInvs}")
        print(f"Pontos restantes: {self.pontosDisponiveis}\n")

    def fazerFicha(self):
        
        while(1):
            print("\nadicionar pericia (1)")
            print("Adicionar habilidade(2)")
            print("Adicionar vantagem (3)")
            print("Adicionar poder (4)")
            print("Adicionar componente em um poder(5) ")
            print("Verificar pontos restantes(6)")
            print("Salvar ficha(7) ")
            print("Sair (0)")
            print('\n')
            opc=int(input("Selecione a opção: "))

            match opc:
                case 1:
                    nomePericia=input("Nome da pericia: ")
                    if(self.validar_tudo(nomePericia,self.pericias_oficiais)):
                        habilidade=int(input("Digite o bonus da habilidade correspondente. Ex: forca 4, digite 4: "))
                        pontosInvestidos = int(input("Digite quantos pontos vai investir na pericia: \n"))
                        self.adicionarPericia(nomePericia=nomePericia,habilidade=habilidade,pontosInvs=pontosInvestidos)
                    else:
                        print("Pericia invalida!")
                case 2:
                    print("Habilidades são forca, agilidade, presenca, vigor, intelecto, luta, prontidao e destreza. Cada graduação é 2 pontos, então força 1 custa 2 pontos de poder\n")
                    nomeHabilidade=input("Nome da habilidade: ")
                    if(self.validar_tudo(nomeHabilidade,self.habilidades_oficiais)):
                        pontosInvestidos=int(input("digite quantas graduações vai investir na habilidade: \n"))
                        self.adicionarHabilidades(nomeHabilidade=nomeHabilidade,gra=pontosInvestidos)
                    else:
                        print("\nHabilidade invalida!")

                case 3:
                    print("Vantagens são normalmente compras únicas,então apenas é necessário 1 ponto, porém algumas podem ter nivel, atente-se!\n")
                    nomeVantagem=input("Digite o nome da vantagem: ")
                    if(self.validar_tudo(nomeVantagem,self.vantagens_oficiais)):
                        pontosInvestidos=int(input("Digite quantos pontos vai investir: \n"))
                        self.adicionarVantagem(nomeVantagem=nomeVantagem,graduacao=pontosInvestidos)
                    else:
                        print("\nVantagem invalida!")
                        

                case 4:
                    print("Em M&M, o poder é criado por seus componetes, entao nessa primeira parte se refere ao nome do conjunto. Ex: raio laser")
                    nomePoder=input("Digite o nome do poder: ")
                    self.adicionarPoder(nomePoder=nomePoder)

                
                case 5:
                    if not self.poderes:
                        print("Nenhum poder criado. Primeiro adicione um poder (opção 4).")
                        break

                    print("\nPoderes existentes:")
                    for i, p in enumerate(self.poderes):
                        print(f"{i+1} - {p['nome']}")

                    escolha = input("\nDigite o número do poder ou pressione ENTER para digitar o nome: ")

                    poder_encontrado = None

                    # Escolha por número (seguro)
                    if escolha.isdigit():
                        indice = int(escolha) - 1
                        if 0 <= indice < len(self.poderes):
                            poder_encontrado = self.poderes[indice]
                        else:
                            print("Número inválido!")
                            break

                    # Escolha por nome (fallback)
                    else:
                        nomePoder = escolha.strip().lower()
                        for poder in self.poderes:
                            if poder["nome"].lower() == nomePoder:
                                poder_encontrado = poder
                                break
                        if not poder_encontrado:
                            print("Poder não encontrado!")
                            break

                    # Agora coleta os dados do componente
                    nomeComponente = input("Nome do componente: ")
                    efeito = input("Efeito: ")
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

                    self.pontosDisponiveis -= (custo_base + sum(extras) - sum(falhas)) * graduacao

                    print(f"\nComponente '{nomeComponente}' adicionado ao poder '{poder_encontrado['nome']}'!")
                    print(f"Pontos restantes: {self.pontosDisponiveis}\n")
                
                
                
                
                # case 5:
                #     nomePoder = input("Digite o nome do poder que deseja adicionar o componente: ")
                #     # procura o poder pelo nome
                #     poder_encontrado = None
                #     for poder in self.poderes:
                #         if poder["nome"].lower() == nomePoder.lower():
                #             poder_encontrado = poder
                #             break
                #     if not poder_encontrado:
                #         print("Poder não encontrado!")
                #     else:
                #         # pedir info do componente
                #         nomeComponente = input("Digite o nome do componente: ")
                #         efeito = input("Digite o efeito: ")
                #         graduacao = int(input("Digite a graduação: "))
                #         custo_base = int(input("Digite o custo base: "))
                #         escolha = input("Vai ter falhas ou extras? 0(não) / 1(sim): ")

                #         extras, falhas = [], []
                #         if escolha == "1":
                #             falhas = list(map(int, input("Digite a lista de falhas: ").strip("[]").split(",")))
                #             extras = list(map(int, input("Digite a lista de extras: ").strip("[]").split(",")))

                #         # adiciona o componente ao poder encontrado
                #         self.adicionarComponente(nomeComponente, efeito, graduacao, custo_base, extras, falhas)

                case 6:
                    print(f"\nVocê possui {self.pontosDisponiveis} pontos disponiveis! \n")

                case 7:
                    variavel_arquivo=input("Digite o nome do arquivo: ")
                    variavel_arquivo_feita = f"{variavel_arquivo}.json"
                    self.salvar(arquivo=variavel_arquivo_feita)

                case 0:
                    return

    def menu(self):
        while(1):
            print("Fazer ficha (1): ")
            print("Carregar ficha (2)")
            print("mensagem misteriosa (3)")
            
            opc = int(input("Escolhe ai: "))
            match opc:
                case 1:
                    self.fazerFicha()
                case 2:
                    caminho=input("Digite o nome da fica,tal qual, Não coloque o .json: ")
                    caminho_feito=f"{caminho}.json"
                    ficha=Ficha.carregar_ficha(caminho=caminho_feito)
                    print("Ficha carregada")
                    ficha.fazerFicha()




np=10
nomePersonagem="teste"
nomeJogador="Kauã"
ficha=Ficha(np=np,nomePersonagem=nomePersonagem,nomeJogador=nomeJogador)

ficha.menu()