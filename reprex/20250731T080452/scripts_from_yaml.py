from frictionless import Package
import os

# Carregar o datapackage.yaml
package = Package('datapackage.yaml')

# Gerar diagrama ER
package.to_er_diagram(path='erd2.dot')
os.system("dot -Tpng erd2.dot > package_erd2.png")

print("Diagrama ER gerado com sucesso!")
print("Tabelas no datapackage:")
for resource in package.resources:
    print(f"- {resource.name}") 