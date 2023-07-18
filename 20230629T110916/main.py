from frictionless import Package
from rich import print_json

dp = Package('datapackage.json')
r = dp.get_resource('1501')
print_json(data = r.read_rows())
