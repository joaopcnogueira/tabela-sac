# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_cli.ipynb.

# %% auto 0
__all__ = ['gerar_tabela_sac', 'install_package']

# %% ../nbs/02_cli.ipynb 2
import os
from fastcore.script import call_parse
from .core import SACCalculator

# %% ../nbs/02_cli.ipynb 3
@call_parse
def gerar_tabela_sac(valor_financiado:float, # Valor financiado
                     prazo:int,              # Prazo em meses
                     taxa_juros:float,       # Taxa de juros ao mês (ex: 0.01 para uma taxa de 1% ao mês)
                     path:str='.'
):
    "Gera a tabela SAC para o valor financiado, prazo e taxa de juros informados."

    sac = SACCalculator(valor_financiado, prazo, taxa_juros)
    tabela = sac.tabela()

    tabela.to_csv(f'{path}/tabela_sac.csv', sep=';', index=False)

    return True

# %% ../nbs/02_cli.ipynb 5
@call_parse
def install_package():
    "Install the package"
    os.system("pip install -e '.[dev]'")
