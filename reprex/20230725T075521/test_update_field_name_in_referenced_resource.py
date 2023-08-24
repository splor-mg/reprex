from frictionless import transform, steps, Package
from pprint import pprint

def test():
    dp = Package('datapackage.json')

    transform(dp, steps=[
        steps.resource_transform(name='dim', steps=[
            steps.field_update(name='uo', descriptor={'name': 'uo_cod'})
        ])
    ])

    # foreignKeys[0].reference.fields from uo to uo_cod
    assert dp.get_resource('fact').schema.foreign_keys[0] == {'fields': ['uo_cod'], 'reference': {'fields': ['uo_cod'], 'resource': 'dim'}}
