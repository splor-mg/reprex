from frictionless import transform, steps, Package
from pprint import pprint

dp = Package('https://raw.githubusercontent.com/splor-mg/datapackage-reprex/main/reprex/20230725T075521/datapackage.json')

print(f"{dp.get_resource('fact').validate().valid=}")

transform(dp, steps=[
    steps.resource_transform(name='dim', steps=[
        steps.field_update(name='uo', descriptor={'name': 'uo_cod'})
    ])
])

pprint(dp.get_resource('fact').validate().flatten(['title', 'message']))

dp.to_yaml('datapackage.yaml')
