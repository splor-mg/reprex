from frictionless import Package

# Load the datapackage
package = Package("datapackage.json")

# Publish all resources to SQLite
package.publish("sqlite:///mydatabase.db")
