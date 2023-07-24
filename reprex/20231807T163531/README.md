# Multipart resource

```bash
python main.py
```

```bash
{'valid': True,
 'stats': {'tasks': 1, 'errors': 0, 'warnings': 0, 'seconds': 0.01},
 'warnings': [],
 'errors': [],
 'tasks': [{'name': 'csv',
            'type': 'table',
            'valid': True,
            'place': 'data-raw/alteracoes-orcamentarias_2021.csv (multipart)',
            'labels': ['ANO', 'UO_COD', 'SUPLEMENTACAO', 'ANULACAO'],
            'stats': {'errors': 0,
                      'warnings': 0,
                      'seconds': 0.01,
                      'md5': '644c0900b2159fbdac7ba7b4e96305b9',
                      'sha256': '21667a8bc20699bd18d4fb004b0f5a54b440f10e38cad5437949bf69cebdfcae',
                      'bytes': 394,
                      'fields': 4,
                      'rows': 18},
            'warnings': [],
            'errors': []}]}
{'valid': False,
 'stats': {'tasks': 1, 'errors': 1, 'warnings': 0, 'seconds': 0.088},
 'warnings': [],
 'errors': [],
 'tasks': [{'name': 'excel',
            'type': 'table',
            'valid': False,
            'place': 'data-raw/alteracoes-orcamentarias_2021.xlsx (multipart)',
            'labels': [],
            'stats': {'errors': 1, 'warnings': 0, 'seconds': 0.088},
            'warnings': [],
            'errors': [{'type': 'format-error',
                        'title': 'Format Error',
                        'description': 'Data reading error because of '
                                       'incorrect format.',
                        'message': 'The data source could not be successfully '
                                   'parsed: invalid excel file '
                                   '"data-raw/alteracoes-orcamentarias_2021.xlsx"',
                        'tags': [],
                        'note': 'invalid excel file '
                                '"data-raw/alteracoes-orcamentarias_2021.xlsx"'}]}]}
```