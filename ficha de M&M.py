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


    def fazerFicha(self,):
        
        while(1):
            print("\nadicionar pericia (1)")
            print("Adicionar habilidade(2)")
            print("Adicionar vantagem (3)")
            print("Adicionar poder (4)")
            print("Adicionar componente em um poder(5): \n")
            opc=int(input("Selecione a opção: "))

            match opc:
                case 1:
                    nomePericia=input("Nome da pericia: ")
                    habilidade=int(input("Digite o bonus da habilidade correspondente. Ex: forca 4, digite 4: "))
                    pontosInvestidos = int(input("Digite quantos pontos vai investir na pericia: \n"))
                    ficha.adicionarPericia(nomePericia=nomePericia,habilidade=habilidade,pontosInvs=pontosInvestidos)

                case 2:
                    print("Habilidades se referem aos famosos atributos, inteligencia, agilidade, etc. Cada graduação é 2 pontos, então força 1 custa 2 pontos de poder\n")
                    nomeHabilidade=input("Nome da habilidade: ")
                    pontosInvestidos=int(input("digite quantas graduações vai investir na habilidade: \n"))
                    ficha.adicionarHabilidades(nomeHabilidade=nomeHabilidade,gra=pontosInvestidos)
                
                case 3:
                    print("Vantagens são normalmente compras unicas,então apenas é necessário 1 ponto, porém algumas podem ter nivel, atente-se!\n")
                    nomeVantagem=input("Digite o nome da vantagem: ")
                    pontosInvestidos=int(input("Digite quantos pontos vai investir: \n"))
                    ficha.adicionarVantagem(nomeVantagem=nomeVantagem,graduacao=pontosInvestidos)

                case 4:
                    print("Em M&M, o poder é criado por seus componetes, entao nessa primeira parte se refere ao nome do conjunto. Ex: raio laser")
                    nomePoder=input("Digite o nome do poder: ")
                    ficha.adicionarPoder(nomePoder=nomePoder)

                case 5:
                    nomePoder = input("Digite o nome do poder que deseja adicionar o componente: ")
                    # procura o poder pelo nome
                    poder_encontrado = None
                    for poder in self.poderes:
                        if poder["nome"] == nomePoder:
                            poder_encontrado = poder
                            break
                    if not poder_encontrado:
                        print("Poder não encontrado!")
                    else:
                        # pedir info do componente
                        nomeComponente = input("Digite o nome do componente: ")
                        efeito = input("Digite o efeito: ")
                        graduacao = int(input("Digite a graduação: "))
                        custo_base = int(input("Digite o custo base: "))
                        escolha = input("Vai ter falhas ou extras? 0(não) / 1(sim): ")

                        extras, falhas = [], []
                        if escolha == "1":
                            falhas = list(map(int, input("Digite a lista de falhas: ").strip("[]").split(",")))
                            extras = list(map(int, input("Digite a lista de extras: ").strip("[]").split(",")))

                        # adiciona o componente ao poder encontrado
                        self.adicionarComponente(nomeComponente, efeito, graduacao, custo_base, extras, falhas)


np=10
nomePersonagem="teste"
nomeJogador="Kauã"
ficha=Ficha(np=np,nomePersonagem=nomePersonagem,nomeJogador=nomeJogador)

ficha.fazerFicha()