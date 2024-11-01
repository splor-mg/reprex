library(relatorios)
library(relatoriosOBZ)
library(RcppTOML)
library(dpm)
library(data.table)

#library(jsonlit)
    


# ================================================================
## data import

execucao <- read_datapackage('datapackages/execucao/datapackage.json')
rp <- read_datapackage('datapackages/rp/datapackage.json')
credito <- read_datapackage('datapackages/credito/datapackage.json')
cota <- read_datapackage('datapackages/cota/datapackage.json')
receita <- read_datapackage('datapackages/receita/datapackage.json')
obz <- read_datapackage('datapackages/obz/datapackage.json')
# ================================================================
## config

config <- parseTOML("relationships.toml")

# ======================================================
## tables
tables <- list(
  execucao = list(
    df = execucao,
    key = config$keys["chave_execucao"],
    drop_columns = NULL
  ),
  rp = list(
    df = execucao,
    key = config$keys["chave_execucao"],
    drop_columns = NULL
  ),
  credito = list(
    df = credito,
    key = config$keys["chave_credito"],
    drop_columns = NULL
  ),
  cota = list(
    df = cota,
    key = config$keys["chave_credito"],
    drop_columns = NULL
  ),
  receita = list(
    df = receita,
    key = config$keys["chave_receita"],
    drop_columns = NULL
  )
)

# ================================================================
## create_tables substitui a etapa acima
result <- create_tables('relationships.toml')
link <- create_linktable('relationships.toml')

# ================================================================
## linktable
link <- create_linktable(tables, keys = config$keys)



