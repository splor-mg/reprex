# Minimal reproducible examples

Esse repositório armazena [minimal, reproducible examples (reprex)](https://stackoverflow.com/help/minimal-reproducible-example) construídos pela Assessoria de Dados.

Ao identificar a necessidade de um reprex crie uma nova pasta com nome `YYYYDDMMThhmmss` dentro da pasta reprex. Por exemplo:

```
.
├── reprex/20230327T162719
│ └── README.md
│ └── datapackage.json
```

Se seu reprex usar um data package, você pode [compartilhar ele online](https://frictionlessdata.io/blog/2016/08/29/publish-online/) utilizando o [link do Github para arquivos raw](https://docs.github.com/en/repositories/working-with-files/using-files/viewing-a-file#viewing-or-copying-the-raw-file-content)

- <https://raw.githubusercontent.com/splor-mg/datapackage-reprex/main/20230327T162719/datapackage.json>

Além disso, atualize a lista abaixo.

## Reprex

- [20230512T084359](reprex/20230512T084359)
  - [Missing value on a date column on excel throws validation error · Issue #1503 · frictionlessdata/framework](https://github.com/frictionlessdata/framework/issues/1503)
  - [Reading resource data from excel throws source error · Issue #1504 · frictionlessdata/framework](https://github.com/frictionlessdata/framework/issues/1504)
- [20230629T110916](reprex/20230629T110916): headerRows to skip rows when reading data files
  - [Criar datapackage para painel OBZ · Issue #58 · splor-mg/atividades](https://github.com/splor-mg/atividades/issues/58#issuecomment-1640308565)
- [20230711T100325](reprex/20230711T100325)
  - [Behaviour of resource.write after steps.table\_normalize · frictionlessdata/frictionlessdata.io · Discussion #822](https://github.com/frictionlessdata/frictionlessdata.io/discussions/822)
- [20230713T220342](reprex/20230713T220342): `schema_sync=True` for reading data files with less columns then defined in table schema
- [20230718T183252](reprex/20230718T183252)
- [20231807T163531](reprex/20231807T163531): multipart excel files in datapackage resource
- [20230721T164121](reprex/20230721T164121)
  - [The data resource has an error: properties "path" and "data" is mutually exclusive when calling resource.to\_view() · Issue #1572 · frictionlessdata/frictionless-py](https://github.com/frictionlessdata/frictionless-py/issues/1572)
- [20230725T075521](reprex/20230725T075521)
  - [Update of primaryKey and foreignKeys when field is renamed · Issue #1560 · frictionlessdata/frictionless-py](https://github.com/frictionlessdata/frictionless-py/issues/1560#issuecomment-1649788083)
- [20230731T181821](reprex/20230731T181821): 
  - [Storing numbers in a string field in excel throws validation error · Issue #1576 · frictionlessdata/frictionless-py](https://github.com/frictionlessdata/frictionless-py/issues/1576)
