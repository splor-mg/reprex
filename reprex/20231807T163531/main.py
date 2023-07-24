from frictionless import Package

package = Package('datapackage.yaml')

excel = package.get_resource('excel')
print(excel.validate())


csv = package.get_resource('csv')
print(csv.validate())
