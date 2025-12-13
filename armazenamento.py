import json
def salvar(ficha,arquivo="ficha.json"):
    dados = {
        "np": ficha.np,
        "nomeJogador": ficha.nomeJogador,
        "nomePersonagem": ficha.nomePersonagem,
        "pontosDisponiveis": ficha.pontosDisponiveis,
        "total": ficha.total,
        "poderes": ficha.poderes,
        "habilidades": ficha.habilidades,
        "pericias": ficha.pericias,
        "vantagens": ficha.vantagens
    }
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print("Ficha salva!")


def carregar_ficha(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
    from ficha import Ficha
    ficha = Ficha(nomeJogador=dados["nomeJogador"],np=dados["np"],nomePersonagem=dados["nomePersonagem"])  # cria ficha vazia

    # joga tudo do JSON dentro da ficha
    for chave, valor in dados.items():
        setattr(ficha, chave, valor)

    return ficha
