import json
from poderes import efeitos_poderes_dicionario,efeitos_poderes_lista,vantagens
from ficha import *
from armazenamento import carregar_ficha

def menu():
    while(1):
        print("Fazer ficha (1): ")
        print("Carregar ficha (2)")
        print("mensagem misteriosa (3)")
        
        opc = int(input("Escolhe ai: "))
        match opc:
            case 1:
                
                nomeJogador = input("Nome do jogador: ")
                nomePersonagem = input("Nome do personagem: ")
                np=int(input("Nivel de poder(NP): "))
                print("\n")
                ficha = Ficha(
                        np=np,
                        nomeJogador=nomeJogador,
                        nomePersonagem=nomePersonagem
                    )
                 
                ficha.fazerFicha()
            case 2:
                caminho=input("Digite o nome da fica,tal qual, Não coloque o .json: ")
                caminho_feito=f"{caminho}.json"
                ficha=carregar_ficha(caminho=caminho_feito)
                print("Ficha carregada")
                ficha.fazerFicha()


menu()



