from frictionless import Resource

def test_default_delimiter():

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

    assert {control.delimiter for control in resource.dialect.controls} == {'|'}

def test_default_delimiter_sample_data():

    resource = Resource.from_descriptor(
        {
            "name": "resource",
            "path": "sample-data.csv",
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

    assert {control.delimiter for control in resource.dialect.controls} == {'|'}

def test_explicit_delimiter():

    resource = Resource.from_descriptor(
        {
            "name": "resource",
            "path": "data.csv",
            "format": "csv",
            "encoding": "utf-8",
            "dialect": {
                    "delimiter": ","
            },
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

    assert {control.delimiter for control in resource.dialect.controls} == {'|'}
