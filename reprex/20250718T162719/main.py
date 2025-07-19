from sqlalchemy.schema import CreateTable
engine = create_engine("sqlite:///:memory:")
table = get_metadata().tables["users"]
print(str(CreateTable(table).compile(engine)))
