from frictionless import transform, steps, Package

def test():
    dp = Package('datapackage.json')

    transform(dp, steps=[
        steps.resource_transform(name='fact', steps=[
            steps.field_update(name='id', descriptor={'name': 'pkey'})
        ])
    ])

    assert dp.get_resource('fact').schema.primary_key == ['pkey']
