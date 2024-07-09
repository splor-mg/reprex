from frictionless import Package
from datetime import datetime

def build_package(descriptor: str = 'datapackage.yaml'):
    
    source = Package(descriptor)

    target_descriptor = {
        "name": source.name,
        "resources": [
            {
            "name": resource_name,
            "path": f'data/{resource_name}.csv',
            "format": "csv",
            "encoding": "utf-8",
            "schema": f"schemas/{resource_name}.yaml"
            } for resource_name in source.resource_names
        ]
    }

    target = Package.from_descriptor(target_descriptor)
    target.custom['updated_at'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    
    for resource in target.resources:
        resource.dereference()
        resource.infer(stats=True)

    target.to_json('datapackage.json')

build_package()
