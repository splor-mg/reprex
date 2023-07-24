from frictionless import Resource, steps, Pipeline

pipeline = Pipeline(steps=[
        steps.field_update(name='id', descriptor = {'name': 'pkey', 'title': 'Primary Key'}),
        steps.row_filter(formula='name != "france"'),
        steps.table_write(path='output.csv'),
        steps.resource_update(name='data', descriptor={'path': 'output.csv'}),
    ])

resource = Resource(path='https://raw.githubusercontent.com/frictionlessdata/frictionless-py/d6f2552b4fd950f459130eda9cf80ae0b8b4931e/data/transform.csv')
resource.transform(pipeline)
resource.infer(stats=True)

print(f'{resource=}')
