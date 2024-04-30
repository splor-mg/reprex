# Skip blank-label error in CLI

```bash
frictionless validate --skip-errors "blank-label" data.csv 
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
frictionless validate --skip-errors "blank-label" datapackage.json
```