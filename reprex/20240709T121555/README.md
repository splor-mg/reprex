I did not find this information in the documentation, but by extrapolating this behavior:

>> Also, won't resource.infer() reset the whole schema of the resource?
> 
> No, it will not change existing properties except for the recalculation of resource.stats.
> 
> -- https://github.com/frictionlessdata/frictionless-py/issues/450#issuecomment-704747085

I assumed that `resource.infer(stats=True)` would not change `dialect.delimiter` (even if it was not explicitly set).

However, this is not the case, and data like:

```
pkey,year,code,desc
2008|1001,2008,1001,PROGRAMA LARES HABITACAO POPULAR
2008|1003,2008,1003,DIVULGACAO DE MINAS GERAIS COMO ESTADO DESCOMPLICADO
```

is causing `resource.infer(stats=True)` to set `dialect.delimiter` to `|`.

There is a reproducible example here.
