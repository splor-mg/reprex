from frictionless import transform, steps, Package

def test():
    dp = Package('datapackage.json')
    resource = dp.get_resource('fact')

    transform(resource, steps=[
        steps.field_update(name='uo_cod', descriptor={'name': 'unidade'})
    ])

    # foreignKeys[0].fields from uo_cod to uo
    assert resource.schema.foreign_keys[0] == {'fields': ['unidade'], 'reference': {'fields': ['uo'], 'resource': 'dim'}}
