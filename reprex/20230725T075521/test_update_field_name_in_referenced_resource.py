from frictionless import transform, steps, Package
from pprint import pprint

def test():
    dp = Package('datapackage.json')

    pprint(dp.get_resource('fact').schema.foreign_keys)
    pprint(dp.get_resource('dim').schema.get_field('uo'))

    transform(dp, steps=[
        steps.resource_transform(name='dim', steps=[
            steps.field_update(name='uo', descriptor={'name': 'uo_cod'})
        ])
    ])

    assert dp.get_resource('fact').schema.foreign_keys[0] == {'fields': ['uo_cod'], 'reference': {'fields': ['uo_cod'], 'resource': 'dim'}}
