from frictionless import Package

def test():
    dp = Package('datapackage.yaml')
    resource = dp.get_resource('csv')
    actual = resource.read_rows()
    expected = [{'a': '1', 'b': '3'}, {'a': '2', 'b': '4'}]
    assert actual == expected
