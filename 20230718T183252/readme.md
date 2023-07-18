# Erros using custom step remove_blank_lines


```
error_change_col_names.py

Arquivo raw: "data-raw/"2101.xlsx
Nrows 5764
-------------------------------------------------------------------------------
CASO 2: deleta linhas em branco corretamente, mas não corrige nomes das colunas.
Salva arquivo com etl.to_csv(), pois utilizar o step table_write_normalized() gera o erro do CASO 1

Arquivo Salvo: 2101.csv 
nrows: 679 
Columns:['UNIDADE ORÇAMENTÁRIA' 'N2' 'SUB SIGLA' 'N3' 'PROGRAMAUO' 'PROGRAMA'
 'prog cod' 'AÇÃO' 'ELEMENTO' 'elem cod' 'ELEMENTO_ITEM' 'elem_cod'
 'Agrupamento' 'GRUPO' 'FONTEUO' 'FONTE (OPCIONAL)'
 'DESCRIÇÃO DO ITEM (OPCIONAL)' 'NOVO?' 'PREMISSA VOLUME' 'VOLUME'
 'PREMISSA DE PREÇO' 'PREÇO UNITÁRIO' 'FREQUÊNCIA PAGAMENTO'
 'VALOR TOTAL ITEM' 'CLASSIFICAÇÃO CENÁRIO' 'DESCRIÇÃO DO CENÁRIO'
 'RISCO DE NÃO FAZER' 'BENEFICIO AO FAZER' 'PRIORIDADE N3' 'PRIORIDADE N2'
 'PRIORIDADE N1']
 

Process finished with exit code 0

```

Descobri o problema usando o snippet abaixo:

```python
from frictionless import Package, Resource, Step, transform, steps, Pipeline, Field
import petl as etl
from dpm.steps import field_rename_to_target, table_write_normalized
from scripts.customsteps import remove_blank_rows
import pandas as pd
import warnings

data_package = Package('datapackage.yaml')
output_path = 'data/'
resource_name = '2281'
resource = data_package.get_resource(resource_name)
warnings.simplefilter(action='ignore', category=UserWarning)
df_excel = pd.read_excel(f'data-raw/{resource.name}.xlsx', sheet_name='BASE OBZ')

print(f'Arquivo raw: "data-raw/"{resource.name}.xlsx')
print(f'Nrows {len(df_excel)}')
print('-------------------------------------------------------------------------------')
print('CASO 1: salva e troca nomes das colunas corretamente.\nConsegue utilizar table_write_normalized(), porém apaga linhas que não devia.\n')

pipeline = Pipeline(steps=[remove_blank_rows(20),
                           field_rename_to_target(),
                           table_write_normalized(output_dir=output_path)])
resource.transform(pipeline)
df = pd.read_csv(f'data/{resource.name}.csv')
print(f'Arquivo Salvo: {resource.name}.csv \nnrows: {len(df)} \nColumns:{str(df.columns)}\n ')

print('-------------------------------------------------------------------------------')

```

```
error_delete_wong_rows.py

Arquivo raw: "data-raw/"2281.xlsx
Nrows 138
-------------------------------------------------------------------------------
CASO 1: salva e troca nomes das colunas corretamente.
Consegue utilizar table_write_normalized(), porém apaga linhas que não devia.

Arquivo Salvo: 2281.csv 
nrows: 38 
Columns:['uo' 'n2' 'sub_sigla_dummy' 'n3' 'dummy_programauo' 'programa'
 'dummy_prog_cod' 'acao' 'elemento' 'dummy_elem_cod' 'elemento_item'
 'dummy_elem_cod_2' 'agrupamento' 'grupo' 'dummy_fonte_uo' 'fonte_cod'
 'descricao_do_item' 'is_new_item' 'premissa_volume' 'volume'
 'premissa_de_preco' 'vr_unitario' 'freq_pagamento' 'vr_total_item'
 'classificacao_cenario' 'descricao_do_cenario' 'risco_de_nao_fazer'
 'beneficio_ao_fazer' 'prioridade_n3' 'prioridade_n2' 'prioridade_n1']

Process finished with exit code 0

```

Descobri o problema usando o snippet abaixo:

```python
from frictionless import Package, Resource, Step, transform, steps, Pipeline, Field
from dpm.steps import field_rename_to_target, table_write_normalized
from scripts.customsteps import remove_blank_rows
import pandas as pd
import warnings

data_package = Package('datapackage.yaml')
output_path = 'data/'
resource_name = '2281'
resource = data_package.get_resource(resource_name)
warnings.simplefilter(action='ignore', category=UserWarning)
df_excel = pd.read_excel(f'data-raw/{resource.name}.xlsx', sheet_name='BASE OBZ')

print(f'Arquivo raw: "data-raw/"{resource.name}.xlsx')
print(f'Nrows {len(df_excel)}')
print('-------------------------------------------------------------------------------')
print('CASO 1: Salva arquivo e troca nomes das colunas corretamente.\nConsegue utilizar table_write_normalized(), porém apaga linhas que não devia.\n')

pipeline = Pipeline(steps=[remove_blank_rows(20),
                           field_rename_to_target(),
                           table_write_normalized(output_dir=output_path)])
resource.transform(pipeline)
df = pd.read_csv(f'data/{resource.name}.csv')
print(f'Arquivo Salvo: {resource.name}.csv \nnrows: {len(df)} \nColumns:{str(df.columns.values)}\n ')


```

O erro acima também apaga linhas indevidas dos outros arquivos Raw. Entendo que o problema seja causado por uso errôneo do generator criado no custom step remove_blank_rows(). Buscou-se substituir o uso desse custom step pelo step filter do frictionless para corrigir o problema.

