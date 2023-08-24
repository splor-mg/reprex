from frictionless import transform, steps, Package

def test():
    dp = Package('datapackage.json')

    transform(dp, steps=[
        steps.resource_transform(name='fact', steps=[
            steps.field_update(name='uo_cod', descriptor={'name': 'uo'})
        ])
    ])

    # foreignKeys[0].fields from uo_cod to uo
    assert dp.get_resource('fact').schema.foreign_keys[0] == {'fields': ['uo'], 'reference': {'fields': ['uo'], 'resource': 'dim'}}
