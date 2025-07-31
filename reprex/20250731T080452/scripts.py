from frictionless import describe
import os

# Descrever todos os arquivos CSV na pasta data
package = describe('data/*')

# Definir chaves primárias
package.get_resource("servidores_ativos").schema.primary_key = ["id"]
package.get_resource("servidores_historico").schema.primary_key = ["id"]

# Definir chaves únicas para servidores_ativos
package.get_resource("servidores_ativos").schema.unique_keys = [
    {"fields": ["cpf"]},
    {"fields": ["masp"]}
]

# Definir chaves estrangeiras para_servidores_historico
package.get_resource("servidores_historico").schema.foreign_keys = [
    {"fields": ["servidor_id"], "reference": {"resource": "servidores_ativos", "fields": ["id"]}}
]

# Gerar diagrama ER
package.to_er_diagram(path='erd.dot')
os.system("dot -Tpng erd.dot > package_erd.png")

# Salvar datapackage.yaml
package.to_yaml("datapackage.yaml") 