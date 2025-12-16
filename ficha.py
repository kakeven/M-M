import json
from poderes import efeitos_poderes_dicionario,efeitos_poderes_lista,vantagens,pericias_por_habilidade,extras_dict
from ficha_utilitarios import( simplificar_pericia, simplificar_habilidade,
simplificar_vantagem, simplificar_componente,simplificar_extraComponente,verificar_digito,simplificar_falhaComponente)

class Ficha:
    def __init__(self,np,nomeJogador,nomePersonagem):
        
        self.np = np
        pontos_por_np = np*15
        self.total = pontos_por_np         
        self.pontosDisponiveis = self.total
        self.nomeJogador=nomeJogador
        self.nomePersonagem=nomePersonagem

        self.poderes=[]
        self.habilidades={
            "forca": 0,
            "agilidade": 0,
            "destreza": 0,
            "luta": 0,
            "intelecto": 0,
            "prontidao": 0,
            "presenca": 0,
            "vigor":0
        }
        self.pericias=[]
        self.vantagens=[]
        self.poderes_lista= efeitos_poderes_lista
        self.poderes_dict = efeitos_poderes_dicionario

        self.habilidades_oficiais = [
        "forca", "agilidade", "presenca", "vigor",
        "intelecto", "luta", "prontidao","destreza"
        ]

        self.pericias_oficiais = [
            "acrobacia", "atletismo","combate a distancia","combate a corpo-a-corpo","enganacao","especialidade",
            "furtividade","intimidacao", "intuicao","investigacao", "percepcao","persuasao","prestidigitacao", 
            "tecnologia","tratamento","veiculos" 
        ]

        self.vantagens_oficiais = vantagens

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

    def adicionarComponente(self, nomeComponente, efeito, graduacao, custo_base):
             # ex: [-1]

        # custo por graduação já modificado
        custo_grad_final = custo_base 

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
            "extras": {},
            "falhas": {},
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
            self.habilidades[nomeHabilidade] += gra

            #Re calcular pericia

            for p in self.pericias:
                habilidade_base = pericias_por_habilidade[p["nome"]]
                if habilidade_base == nomeHabilidade:
                    p["bonus"] = p["graduação"] + self.habilidades[nomeHabilidade]
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

    def adicionarExtrasComponentes(self,nomeComponente,efeito_extra,graduacao=1):
        #pegar o componente escolhido
        for poder in self.poderes:
            for componente in poder["componentes"]:
                if componente["nome"]== nomeComponente:
                    if "extras" not in componente:
                        componente["extras"] = {}

                    componente["extras"][efeito_extra] = graduacao
                    return 

    def adicionarExtrasPoderes(self,nomePoder,efeito_extra,graduacao=1):
        for poder in self.poderes:
            if nomePoder==poder["nome"]:
                poder[efeito_extra][graduacao]
                
                if "extras" not in poder:
                    poder["extras"]= {}
        
                poder["extras"][efeito_extra] = graduacao
                return

    def adicionarFalhasComponentes(self,nomeComponente,efeito_falha,graduacao=-1):
        #pegar o componente escolhido
        for poder in self.poderes:
            for componente in poder["componentes"]:
                if componente["nome"]== nomeComponente:
                    if "falhas" not in componente:
                        componente["falhas"] = {}

                    componente["falhas"][efeito_falha] = graduacao
                    return 

    def fazerFicha(self):
        from armazenamento import salvar
        while(1):
            print("\nadicionar pericia (1)")
            print("Adicionar habilidade(2)")
            print("Adicionar vantagem (3)")
            print("Adicionar poder (4)")
            print("Adicionar componente em um poder (5) ")
            print("Verificar pontos restantes(6)")
            print("Salvar ficha(7) ")
            print("Adicionar Extras ou falhas(8)")
            print("Sair (0)")
            print('\n')
            opc= verificar_digito("Escolha por numero: ")

            match opc:
                case 1:
                    simplificar_pericia(self)
                case 2:
                    simplificar_habilidade(self)
                case 3:
                    simplificar_vantagem(self)
                case 4:
                    print("Em M&M, o poder é criado por seus componetes, entao nessa primeira parte se refere ao nome do conjunto. Ex: raio laser")
                    nomePoder=input("Digite o nome do poder: ")
                    self.adicionarPoder(nomePoder=nomePoder)
                case 5:
                    simplificar_componente(self)
                                     
                case 6:
                    print(f"\nVocê possui {self.pontosDisponiveis} pontos disponiveis! \n")
                case 7:
                    variavel_arquivo=input("Digite o nome do arquivo: ")
                    variavel_arquivo_feita = f"{variavel_arquivo}.json"
                    salvar(self,arquivo=variavel_arquivo_feita)
                case 8:
                    print("adicionar extra em componente (1)")
                    print("Adicionar extra em poder (2)Nao funciona ainda")
                    print("adicionar falha em componente (3)")
                    print("adicionar falha em poder (4)Nao funciona ainda")
                    
                    opc= verificar_digito("Escolha por numero: ")
                    match opc:
                        case 1:
                            simplificar_extraComponente(self)


                        case 3:
                            simplificar_falhaComponente(self)
                case 0:
                    return
