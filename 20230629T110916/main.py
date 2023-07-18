from frictionless import Package

dp = Package('datapackage.json')
print(dp.get_resource('1501').to_view())
print(dp.get_resource('1501').validate())
