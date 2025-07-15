from frictionless import Package
import os

package = Package('datapackage.yaml')
package.to_er_diagram(path='erd2.dot')
os.system("dot -Tpng erd.dot > package_erd2.png")