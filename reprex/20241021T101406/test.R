library(dpm)

library(dpm)
library(data.table)
library(relatorios)
library(relatoriosOBZ)
library(RcppTOML)
library(jsonlite)

# ================================================================
## data import

execucao <- fread('data/exec.csv')
rp <- fread('data/rp.csv') 
credito <- fread('data/credito.csv')
cota <- fread('data/cota.csv')
receita <- fread('data/receita.csv')

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
## linktable
link <- create_linktable(tables, keys = config$keys)

