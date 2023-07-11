from frictionless import Resource, transform, steps

resource = Resource('resource.yaml')

transform(resource, steps=[steps.table_normalize()])

resource.write('output-frictionless.csv')
resource.to_petl().tocsv('output-petl.csv')
