# skip rows with headerRows

```
python main.py 
+-------------------------------------+---------------------------+-------------------------------------------+
| UNIDADE ORÇAMENTÁRIA                | PROGRAMA                  | ELEMENTO                                  |
+=====================================+===========================+===========================================+
| 'Fundação de Artes de Minas Gerais' | '060 - FORMACAO CULTURAL' | '14 - DIÁRIAS - CIVIL'                    |
+-------------------------------------+---------------------------+-------------------------------------------+
| 'Fundação de Artes de Minas Gerais' | '060 - FORMACAO CULTURAL' | '33 - PASSAGENS E DESPESAS COM LOCOMOÇÃO' |
+-------------------------------------+---------------------------+-------------------------------------------+
| 'Fundação de Artes de Minas Gerais' | '060 - FORMACAO CULTURAL' | '14 - DIÁRIAS - CIVIL'                    |
+-------------------------------------+---------------------------+-------------------------------------------+
| None                                | None                      | None                                      |
+-------------------------------------+---------------------------+-------------------------------------------+

{'valid': False,
 'stats': {'tasks': 1, 'errors': 1, 'warnings': 0, 'seconds': 0.004},
 'warnings': [],
 'errors': [],
 'tasks': [{'name': '1501',
            'type': 'table',
            'valid': False,
            'place': '1501.xlsx',
            'labels': ['UNIDADE ORÇAMENTÁRIA', 'PROGRAMA', 'ELEMENTO'],
            'stats': {'errors': 1,
                      'warnings': 0,
                      'seconds': 0.004,
                      'md5': '2e3dd27c5470d02a851319a73e3e053b',
                      'sha256': '8e5e455e763091c39adc3195c94fefd41f2524e1549f3e185aae143d065eb819',
                      'bytes': 14118,
                      'fields': 3,
                      'rows': 4},
            'warnings': [],
            'errors': [{'type': 'blank-row',
                        'title': 'Blank Row',
                        'description': 'This row is empty. A row should '
                                       'contain at least one value.',
                        'message': 'Row at position "6" is completely blank',
                        'tags': ['#table', '#row'],
                        'note': '',
                        'cells': ['', '', ''],
                        'rowNumber': 6}]}]}
```

Descobri o problema usando o snippet abaixo:

```python
from frictionless import Resource, Dialect, formats

control=formats.ExcelControl(sheet='BASE OBZ')
dialect = Dialect(header_rows=[2])

r = Resource('1501.xlsx', dialect=dialect, control=control)
print(r)
```