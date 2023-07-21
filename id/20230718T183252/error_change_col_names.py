from frictionless import Package, Resource, Step, transform, steps, Pipeline, Field
import petl as etl
from dpm.steps import field_rename_to_target, table_write_normalized
from scripts.customsteps import remove_blank_rows
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)

data_package = Package('datapackage.yaml')
output_path = 'data/'
resource_name = '2101'
resource = data_package.get_resource(resource_name)


df_excel = pd.read_excel(f'data-raw/{resource.name}.xlsx', sheet_name='BASE OBZ')

print(f'Arquivo raw: "data-raw/"{resource.name}.xlsx')
print(f'Nrows {len(df_excel)}')
print('-------------------------------------------------------------------------------')
print('CASO 2: deleta linhas em branco corretamente, mas não corrige nomes das colunas.'
      '\nSalva arquivo com etl.to_csv(), pois utilizar o step table_write_normalized() gera o erro do CASO 1\n')

pipeline = Pipeline(steps=[remove_blank_rows(20),
                           field_rename_to_target()])
resource.transform(pipeline)
target = resource.to_copy()
table = target.to_petl()
etl.tocsv(table, output_path + resource.name + '.csv', encoding='utf-8')


df = pd.read_csv(f'data/{resource.name}.csv')
print(f'Arquivo Salvo: {resource.name}.csv \nnrows: {len(df)} \nColumns:{df.columns.values}\n ')



# # caso 3: Apaga linhas em branco, mas também linhas que não devia. Como está sem field_rename_to_target() não muda os nomes
# pipeline = Pipeline(steps=[remove_blank_rows(20),
#                           table_write_normalized(output_dir=output_path)])
# resource.transform(pipeline)

# caso 3: Salva e troca nomes das colunas. Como está sem remove_blank_rows, mantem linhas em branco
# pipeline = Pipeline(steps=[field_rename_to_target(), table_write_normalized(output_dir=output_path)])
# resource.transform(pipeline)


""" 
 Ao converter para petl os nomes das colunas não sao substituidos corretamente.
 Steps do DPM não estão funcionando junto do remove blank lines, trocar por row_filter().

"""