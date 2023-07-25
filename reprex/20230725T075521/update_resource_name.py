from frictionless import transform, steps, Package
from pprint import pprint

dp = Package('datapackage.json')

print(f"{dp.get_resource('fact').validate().valid=}")

transform(dp, steps=[
    steps.resource_transform(name='dim', steps=[
        steps.resource_update(name='dim', descriptor={'name': 'dm'})
    ])
])

pprint(dp.get_resource('fact').validate().flatten(['title', 'message']))
