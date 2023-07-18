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



