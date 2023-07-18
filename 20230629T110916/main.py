from frictionless import Package, Resource, Dialect, formats

dp = Package('datapackage.json')
print(dp.get_resource('1501').to_view())


control=formats.ExcelControl(sheet='BASE OBZ')
dialect = Dialect(header_rows=[2])

r = Resource('1501.xlsx', dialect=dialect, control=control)
print(r.to_view())