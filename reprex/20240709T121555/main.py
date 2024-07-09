from frictionless import Resource

resource = Resource.from_descriptor(
    {
        "name": "resource",
        "path": "data.csv",
        "format": "csv",
        "encoding": "utf-8",
        "schema": {
            "fields": [
                {"name": "pkey", "type": "string"},
                {"name": "year", "type": "integer"},
                {"name": "code", "type": "integer"},
                {"name": "desc", "type": "string"},
            ]
        },
    }
)

resource.infer(stats=True)
print(resource.dialect)
