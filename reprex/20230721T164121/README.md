# README

```bash
python main.py 
```

```bash
resource={'name': 'transform',
 'type': 'table',
 'data': [],
 'scheme': '',
 'format': 'inline',
 'mediatype': 'text/csv',
 'extrapaths': [],
 'schema': {'fields': [{'name': 'pkey',
                        'type': 'integer',
                        'title': 'Primary Key'},
                       {'name': 'name', 'type': 'string'},
                       {'name': 'population', 'type': 'integer'}]}}
Traceback (most recent call last):
  File "/Users/fjunior/Projects/splor/datapackage-reprex/reprex/20230721T164121/venv/lib/python3.11/site-packages/frictionless/transformer/transformer.py", line 86, in __iter__
    yield from self.data() if callable(self.data) else self.data
TypeError: 'NoneType' object is not iterable

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/fjunior/Projects/splor/datapackage-reprex/reprex/20230721T164121/venv/lib/python3.11/site-packages/frictionless/formats/inline/parser.py", line 48, in read_cell_stream_create
    item = next(data)
           ^^^^^^^^^^
  File "/Users/fjunior/Projects/splor/datapackage-reprex/reprex/20230721T164121/venv/lib/python3.11/site-packages/frictionless/transformer/transformer.py", line 92, in __iter__
    raise FrictionlessException(error) from exception
frictionless.exception.FrictionlessException: [step-error] Step is not valid: "resource_update" raises "'NoneType' object is not iterable" 
```