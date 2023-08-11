from frictionless import Resource, transform, steps

resource = Resource('https://raw.githubusercontent.com/splor-mg/datapackage-reprex/main/reprex/20230711T100325/resource.yaml')

transform(resource, steps=[steps.table_normalize()])

resource.write('output-frictionless.csv')
resource.to_petl().tocsv('output-petl.csv')
