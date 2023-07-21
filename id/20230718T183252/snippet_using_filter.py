from frictionless import Package, Resource, steps, transform, Field
import petl as etl

data_package = Package(resources=[Resource(path='data-raw/test_data.xlsx', name='base-obz')])

print(data_package.get_resource('base-obz').to_view())
print(data_package.get_resource('base-obz'))


source = data_package.get_resource('base-obz')
target = transform(
    source,
    steps=[
        steps.table_normalize(),
        steps.row_filter(formula="id != None and variable != None and value != None")
    ]
)

table = target.to_petl()

etl.tocsv(table, 'data/filtered_test_data.csv', encoding='utf-8')

print(target.schema)
print(target.to_view())