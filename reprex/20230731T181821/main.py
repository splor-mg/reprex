from frictionless import Package

dp = Package('datapackage.yaml')
print(dp.get_resource('excel').read_rows())
