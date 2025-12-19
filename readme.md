# Projeto de ficha — Mutantes & Malfeitores (3ª edição)

Projeto de criação de fichas para o RPG **Mutantes & Malfeitores 3ª edição**.

## Observações
O projeto não segue o material oficial à risca.

As falhas são aplicadas ao **poder como um todo**, não por faixas de graduação.

Exemplo:  
- Poder: Kit Superman  
- Componente: Voo (Graduação 10)  
- Falha: Cansativo  

Nesse caso, o personagem ficará cansado **em qualquer nível de voo**.  
No livro, a falha poderia ser aplicada apenas às graduações 9 e 10.

Essa simplificação foi uma decisão de design.

## Observação sobre seleção de dados

A seleção de **itens, vantagens, perícias e habilidades** é feita por meio de **números**.

Essa abordagem foi adotada para:
- Padronizar a escrita dos dados
- Evitar erros humanos de digitação
- Garantir consistência no JSON gerado
- Facilitar validações e cálculos automáticos


## Equipamentos
A vantagem **Equipamentos** ainda não possui dados completos.

Atualmente, não é possível adicionar:
- Veículos
- Propriedades
- Outros itens complexos

Essa funcionalidade será adicionada futuramente.

## Funcionalidades Ativas
- Criar, salvar e carregar personagens
- Criação completa de poderes
- Aplicação de custos de falhas e extras
- Cálculos da ficha totalmente automatizados

## Planejado
- Exportação para PDF
- Funcionalidade completa de Equipamentos
- Interface gráfica
- Edição direta da ficha

## Exemplo de ficha (JSON)

Segue um exemplo de ficha utilizando **todas as funcionalidades atualmente disponíveis** no projeto:

```json
{
  "np": 10,
  "nomeJogador": "kaua",
  "nomePersonagem": "Kaleo",
  "pontosDisponiveis": 17,
  "total": 150,
  "poderes": [
    {
      "nome": "composto K",
      "componentes": [
        {
          "nome": "forca",
          "efeito": "Característica Aumentada",
          "graduacao": 10,
          "custo_base": 2,
          "extras": {},
          "falhas": {},
          "mod_por_graduacao": 0,
          "mod_fixo": 0,
          "custo_total": 20
        },
        {
          "nome": "voo",
          "efeito": "Voo",
          "graduacao": 10,
          "custo_base": 2,
          "extras": {},
          "falhas": {
            "cansativo": {
              "tipo": "por_graduacao",
              "valor": -1
            }
          },
          "mod_por_graduacao": -1,
          "mod_fixo": 0,
          "custo_total": 10
        },
        {
          "nome": "vigor",
          "efeito": "Característica Aumentada",
          "graduacao": 8,
          "custo_base": 2,
          "extras": {},
          "falhas": {},
          "mod_por_graduacao": 0,
          "mod_fixo": 0,
          "custo_total": 16
        },
        {
          "nome": "fator de cura",
          "efeito": "Regeneração",
          "graduacao": 2,
          "custo_base": 1,
          "extras": {},
          "falhas": {},
          "mod_por_graduacao": 0,
          "mod_fixo": 0,
          "custo_total": 2
        },
        {
          "nome": "sentidos",
          "efeito": "Sentidos",
          "graduacao": 5,
          "custo_base": 1,
          "extras": {},
          "falhas": {},
          "mod_por_graduacao": 0,
          "mod_fixo": 0,
          "custo_total": 5
        },
        {
          "nome": "invulnerabilidade",
          "efeito": "Imunidade",
          "graduacao": 10,
          "custo_base": 1,
          "extras": {},
          "falhas": {},
          "mod_por_graduacao": 0,
          "mod_fixo": 0,
          "custo_total": 10
        },
        {
          "nome": "supervelocidade",
          "efeito": "Supervelocidade",
          "graduacao": 3,
          "custo_base": 3,
          "extras": {},
          "falhas": {},
          "mod_por_graduacao": 0,
          "mod_fixo": 0,
          "custo_total": 9
        },
        {
          "nome": "destreza",
          "efeito": "Característica Aumentada",
          "graduacao": 7,
          "custo_base": 2,
          "extras": {},
          "falhas": {},
          "mod_por_graduacao": 0,
          "mod_fixo": 0,
          "custo_total": 14
        },
        {
          "nome": "agilidade",
          "efeito": "Característica Aumentada",
          "graduacao": 7,
          "custo_base": 2,
          "extras": {},
          "falhas": {},
          "mod_por_graduacao": 0,
          "mod_fixo": 0,
          "custo_total": 14
        },
        {
          "nome": "raio laser",
          "efeito": "Raio",
          "graduacao": 6,
          "custo_base": 2,
          "extras": {
            "alcance estendido": {
              "tipo": "por_graduacao",
              "valor": 3
            }
          },
          "falhas": {
            "concentracao": {
              "tipo": "por_graduacao",
              "valor": -1
            },
            "cansativo": {
              "tipo": "por_graduacao",
              "valor": -1
            }
          },
          "mod_por_graduacao": 1,
          "mod_fixo": 0,
          "custo_total": 18
        }
      ],
      "falhas": {
        "removivel": 1
      }
    }
  ],
  "habilidades": {
    "forca": 0,
    "agilidade": 0,
    "destreza": 0,
    "luta": 0,
    "intelecto": 8,
    "prontidao": 0,
    "presenca": 1,
    "vigor": 0
  },
  "pericias": [
    {
      "nome": "tecnologia",
      "graduacao": 10,
      "bonus": 18,
      "custo": 5
    },
    {
      "nome": "investigacao",
      "graduacao": 4,
      "bonus": 12,
      "custo": 2
    }
  ],
  "vantagens": [
    {
      "nome": "beneficio",
      "graduacao": 6,
      "pontos_gastos": 6
    },
    {
      "nome": "faz tudo",
      "graduacao": 1,
      "pontos_gastos": 1
    },
    {
      "nome": "bem informado",
      "graduacao": 1,
      "pontos_gastos": 1
    },
    {
      "nome": "idiomas",
      "graduacao": 3,
      "pontos_gastos": 3
    },
    {
      "nome": "inventor",
      "graduacao": 1,
      "pontos_gastos": 1
    },
    {
      "nome": "atraente",
      "graduacao": 1,
      "pontos_gastos": 1
    },
    {
      "nome": "ferramentas aprimoradas",
      "graduacao": 1,
      "pontos_gastos": 1
    }
  ]
}
