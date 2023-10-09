import pytest
from frictionless import transform, steps, Package

@pytest.fixture
def package():
    descriptor = {
        "name": "hr",
        "resources": [
            {
                "name": "employees",
                "path": "data-raw/employees.csv",
                "format": "csv",
                "encoding": "utf-8",
                "schema": {
                    "fields": [
                        {"name": "EmployeeID", "type": "integer"},
                        {"name": "Name", "type": "string"},
                        {"name": "DepartmentID", "type": "integer"},
                    ],
                    "primaryKey": ["EmployeeID"],
                    "foreignKeys": [
                        {
                            "fields": ["DepartmentID"],
                            "reference": { "fields": ["DepartmentID"], "resource": "departments" },
                        }
                    ],
                },
            },
            {
                "name": "departments",
                "path": "data-raw/departments.csv",
                "format": "csv",
                "encoding": "utf-8",
                "schema": {
                    "fields": [
                        {"name": "DepartmentID", "type": "integer"},
                        {"name": "DepartmentName", "type": "string"},
                    ],
                    "primaryKey": ["DepartmentID"],
                },
            },
        ],
    }
    result = Package.from_descriptor(descriptor)
    yield result


def test(package):
    resource = package.get_resource("employees")

    assert resource.schema.foreign_keys[0] == {
        "fields": ["DepartmentID"],
        "reference": {"fields": ["DepartmentID"], "resource": "departments"},
    }

    transform(
        resource,
        steps=[
            steps.field_update(
                name="DepartmentID", descriptor={"name": "department_id"}
            )
        ],
    )

    assert resource.schema.foreign_keys[0] == {
        "fields": ["department_id"],
        "reference": {"fields": ["DepartmentID"], "resource": "departments"},
    }
