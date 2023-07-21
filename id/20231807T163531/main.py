import frictionless
from frictionless import Schema, describe
from frictionless import validate
from pprint import pprint
# describe = describe("data-raw/alteracoes-orcamentarias_2021.csv")
# describe.to_yaml("schemas/alteracoes-orcamentarias.yaml")

report = validate('schemas/alteracoes-orcamentarias.yaml')
print(report)






