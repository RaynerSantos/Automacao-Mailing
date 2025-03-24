import pandas as pd 
import numpy as np 
import time
from unidecode import unidecode

data = pd.read_excel("C:\PROJETOS\Automacao Mailing\Listagem Map Preço_ RM.xlsx") 
print(data)
cd_so = 'nu_so_ec'
TELEFONES = 'CD_DDD_TELEFONE_EC, NU_TELEFONE_EC, ddd1, tel1, ddd2, tel2'
TELEFONES = TELEFONES.split(', ')
COLUNAS_PARA_TRATAR = 'mbc, dc_unde_ngco, dc_setr_bigdata, sg_so_uf, nm_so_cidade, porte_fat_pot_base2, nm_repr_venda, nm_fantasia, nm_gestor_conta, nm_cadeia_forcada, MN_MATRIZ_SGMT'
COLUNAS_PARA_TRATAR = COLUNAS_PARA_TRATAR.split(', ')
COLUNAS_NAO_INVALIDAS = 'nu_so_ec'
COLUNAS_NAO_INVALIDAS = COLUNAS_NAO_INVALIDAS.split(', ')
EXCLUIR_TELEFONES_DUPLICADOS = 'SIM'
ALEATORIO = 'SIM'
COLUNA_TEL_CONCAT = 'NAO'

bd_teste = pd.DataFrame({
    'cod': [52, 27, 54, 33, 22, 84, 54],
    'group': ['a', 'a', 'd', 'e', 'b', 'b', 'c'],
    'value': [175.5, 178.2, 157.6, 160.2, 181.1, 197.9, 145.8]
})
print(f'banco original:\n{bd_teste}')
print(f'\nbanco{bd_teste[bd_teste.duplicated(subset='cod', keep='first')]}')

