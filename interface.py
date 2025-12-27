from ficha import Ficha
from armazenamento import carregar_ficha
from ficha_utilitarios import verificar_digito
def menu():
    while(1):
        print("Fazer ficha (1): ")
        print("Carregar ficha (2)")
        print("Sair (0)")
        opc = verificar_digito("Escolha: ")
        
        if opc>3 or opc<0:
            print("\nDigite apenas numeros validos\n")
        else:
            match opc:
                case 1:
                    
                    nomeJogador = input("\nNome do jogador: ")
                    nomePersonagem = input("\nNome do personagem: ")
                    np=verificar_digito("\nNivel de poder(NP): ")
                    print("\n")
                    ficha = Ficha(
                            np=np,
                            nomeJogador=nomeJogador,
                            nomePersonagem=nomePersonagem
                        )
                    ficha.fazerFicha()
                    
                case 2:
                    caminho=input("Digite o nome da ficha,tal qual, Não coloque o .json: ")
                    caminho_feito=f"{caminho}.json"
                    ficha=carregar_ficha(caminho=caminho_feito)
                    print("Ficha carregada")
                    ficha.fazerFicha()

                case 0:
                    return
        



