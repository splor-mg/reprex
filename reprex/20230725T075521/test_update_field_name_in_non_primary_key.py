from frictionless import transform, steps, Package
from pprint import pprint

def test():
    dp = Package('datapackage.json')

    transform(dp, steps=[
        steps.resource_transform(name='fact', steps=[
            steps.field_update(name='hist', descriptor={'name': 'memo'})
        ])
    ])

    assert dp.get_resource('fact').schema
