from frictionless import Resource

acao = Resource.from_descriptor({
    "name": "acao",
    "profile": "tabular-data-resource",
    "path": 'data/acao.csv',
    "format": "csv",
    "encoding": "utf-8",
    "schema": "schemas/acao.yaml"
})

acao.infer(stats=True)
print(acao)

resource = Resource.from_descriptor({
    "name": "resource",
    "path": "data.csv",
    "format": "csv",
    "encoding": "utf-8",
    "schema": {'fields': [{'name': 'chave_acao', 'type': 'string'},
                       {'name': 'ano', 'type': 'integer'},
                       {'name': 'acao_cod', 'type': 'integer'},
                       {'name': 'acao_desc', 'type': 'string'}]}
})

resource.dereference()
resource.infer(stats=True)
print(resource)