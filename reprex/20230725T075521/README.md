# Metadata

```bash
$ python update_resource_name.py 
dp.get_resource('fact').validate().valid=True
[['Resource Error',
  'The data resource has an error: failed to handle a foreign key for resource '
  '"fact" as resource "dim" does not exist']]
```

```bash
$ frictionless validate datapackage.yaml 
─────────────────────────────────────────────────────────────── Dataset ────────────────────────────────────────────────────────────────
                 dataset                  
┏━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ name ┃ type  ┃ path          ┃ status  ┃
┡━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ fact │ table │ data/fact.txt │ INVALID │
│ dm   │ table │ data/dim.txt  │ VALID   │
└──────┴───────┴───────────────┴─────────┘
──────────────────────────────────────────────────────────────── Tables ────────────────────────────────────────────────────────────────
                                                                  fact                                                                  
┏━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Row  ┃ Field ┃ Type           ┃ Message                                                                                              ┃
┡━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ None │ None  │ resource-error │ The data resource has an error: failed to handle a foreign key for resource "fact" as resource "dim" │
│      │       │                │ does not exist                                                                                       │
└──────┴───────┴────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

```bash
$ python update_field_name.py 
dp.get_resource('fact').validate().valid=True
[['ForeignKey Error',
  'Row at position "2" violates the foreign key: for "uo_cod": values "1501" '
  'not found in the lookup table "dim" as "uo"'],
 ['ForeignKey Error',
  'Row at position "3" violates the foreign key: for "uo_cod": values "1251" '
  'not found in the lookup table "dim" as "uo"'],
 ['ForeignKey Error',
  'Row at position "4" violates the foreign key: for "uo_cod": values "1251" '
  'not found in the lookup table "dim" as "uo"']]
```

```bash
$ frictionless validate datapackage.yaml
─────────────────────────────────────────────────────────────── Dataset ────────────────────────────────────────────────────────────────
                 dataset                  
┏━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ name ┃ type  ┃ path          ┃ status  ┃
┡━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ fact │ table │ data/fact.txt │ INVALID │
│ dim  │ table │ <memory>      │ INVALID │
└──────┴───────┴───────────────┴─────────┘
──────────────────────────────────────────────────────────────── Tables ────────────────────────────────────────────────────────────────
                                               fact                                               
┏━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Row  ┃ Field ┃ Type         ┃ Message                                                          ┃
┡━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ None │ None  │ source-error │ The data source has not supported or has inconsistent contents:  │
└──────┴───────┴──────────────┴──────────────────────────────────────────────────────────────────┘
                                               dim                                                
┏━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Row  ┃ Field ┃ Type         ┃ Message                                                          ┃
┡━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ None │ None  │ source-error │ The data source has not supported or has inconsistent contents:  │
└──────┴───────┴──────────────┴──────────────────────────────────────────────────────────────────┘
```
