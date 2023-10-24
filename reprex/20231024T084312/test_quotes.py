from frictionless import Resource
import logging

def test_single_quotes():
    resource = Resource('resource-single-quotes.yaml')
    report = resource.validate()
    logging.warning(report.tasks[0].errors[0].message)
    assert report.valid

def test_double_quotes():
    resource = Resource('resource-double-quotes.yaml')
    report = resource.validate()
    assert report.valid
