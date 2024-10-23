config <- parseTOML("relationships.toml")
tables <- create_tables_list(config)

create_tables_list <- function(config) {

    create_table <- function(resource) {
    df <- data.table::fread(resource$path)  
    key_name <- resource$key_name           
    key <- config$keys[key_name]       
    
    list(
      df = df,            
      key = key,           
      drop_columns = NULL  
    )
  }
  
  tables <- purrr::map(config$data, function(resource) {
    create_table(resource)
  })
  return(tables)
}
