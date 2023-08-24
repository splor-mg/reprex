from frictionless import transform, steps, Package

def test():
    dp = Package('datapackage.json')

    transform(dp, steps=[
        steps.resource_transform(name='dim', steps=[
            steps.resource_update(name='dim', descriptor={'name': 'dm'})
        ])
    ])

    assert dp.get_resource('fact').schema.foreign_keys[0] == {'fields': ['uo_cod'], 'reference': {'fields': ['uo'], 'resource': 'dm'}}
