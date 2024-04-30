# Skip blank-label error in CLI


```bash
frictionless validate --skip-errors "blank-label" https://raw.githubusercontent.com/splor-mg/reprex/main/reprex/20231228T143527/datapackage.json
```

```
────────────────────────────────────────────────────────────── Dataset ───────────────────────────────────────────────────────────────
               dataset               
┏━━━━━━┳━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┓
┃ name ┃ type  ┃ path     ┃ status  ┃
┡━━━━━━╇━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━┩
│ data │ table │ data.csv │ INVALID │
└──────┴───────┴──────────┴─────────┘
─────────────────────────────────────────────────────────────── Tables ───────────────────────────────────────────────────────────────
                                         data                                         
┏━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Row  ┃ Field ┃ Type        ┃ Message                                               ┃
┡━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ None │ 2     │ blank-label │ Label in the header in field at position "2" is blank │
└──────┴───────┴─────────────┴───────────────────────────────────────────────────────┘
```

```bash
frictionless validate --skip-errors "blank-label" https://raw.githubusercontent.com/splor-mg/reprex/main/reprex/20231228T143527/data.csv
```

```
─────────────────────────────────────────────────────── Dataset ────────────────────────────────────────────────────────
              dataset               
┏━━━━━━┳━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┓
┃ name ┃ type  ┃ path     ┃ status ┃
┡━━━━━━╇━━━━━━━╇━━━━━━━━━━╇━━━━━━━━┩
│ data │ table │ data.csv │ VALID  │
└──────┴───────┴──────────┴────────┘
```

```bash
frictionless validate --skip-errors "blank-label" https://raw.githubusercontent.com/splor-mg/reprex/main/reprex/20231228T143527/resource.json
```
