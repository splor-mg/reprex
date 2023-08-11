from frictionless import Resource, transform, steps, Schema

resource = Resource('https://raw.githubusercontent.com/splor-mg/datapackage-reprex/main/reprex/20230711T100325/resource.yaml')
target_schema = Schema('https://raw.githubusercontent.com/splor-mg/datapackage-reprex/main/reprex/20230711T100325/target.yaml')

transform(resource, steps=[steps.table_normalize(), steps.table_write(path='output.csv', schema=target_schema)])