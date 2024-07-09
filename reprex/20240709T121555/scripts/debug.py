from frictionless import Resource

acao = Resource.from_descriptor({
    "name": "acao",
    "path": f'data/acao.csv',
    "format": "csv",
    "encoding": "utf-8",
    "schema": f"schemas/acao.yaml"
})

acao.infer(stats=True)
print(acao)