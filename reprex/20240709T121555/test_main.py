from frictionless import Resource
import pytest

def test_bad_delimiter():

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
