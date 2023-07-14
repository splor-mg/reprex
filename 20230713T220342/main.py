from frictionless import Resource, Schema, Detector

r0 = Resource('data.csv', schema=Schema('schema.yaml'))
r0.validate()
r0.read_rows()


r1 = Resource('data.csv', schema=Schema('schema.yaml'), detector=Detector(schema_sync=True))
r1.validate()
r1.read_rows()