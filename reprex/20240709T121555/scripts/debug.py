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
    "profile": "tabular-data-resource",
    "path": 'data.csv',
    "format": "csv",
    "encoding": "utf-8",
    "schema": "schema.yaml"
})

resource.infer(stats=True)
print(resource)