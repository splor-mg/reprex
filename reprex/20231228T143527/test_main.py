from frictionless import Package, Resource, describe, Checklist

def test_describe_invalid():
    resource = describe('data.csv')
    report = resource.validate()
    assert report.valid == False
    assert report.flatten(['description']) == [['A label in the header row is missing a value. Label should be provided and not be blank.']]
    

def test_empty_string():
    resource = Resource.from_descriptor({
    "name": "data",
    "path": "data.csv",
    "format": "csv",
    "encoding": "utf-8",
    "schema": {
        "fields": [
        {
            "name": "a",
            "type": "integer"
        },
        {
            "name": "",
            "type": "any"
        }
        ]
    }
    }
    )

    report = resource.validate()
    assert report.valid == False
    assert report.flatten(['description']) == [['A label in the header row is missing a value. Label should be provided and not be blank.']]

def test_skip_blank_label_error():
    resource = Resource.from_descriptor({
    "name": "data",
    "path": "data.csv",
    "format": "csv",
    "encoding": "utf-8",
    "schema": {
        "fields": [
        {
            "name": "a",
            "type": "integer"
        },
        {
            "name": "",
            "type": "any"
        }
        ]
    }
    }
    )

    checklist = Checklist(skip_errors=["blank-label"])
    report = resource.validate(checklist)
    assert report.valid == True
    assert resource.read_rows() == [{'a': 1, '': None}, {'a': 2, '': None}]


def test_package_validate_skip_errors():
    package = Package("datapackage.json")
    checklist = Checklist(skip_errors=["blank-label"])
    report = package.validate(checklist)
