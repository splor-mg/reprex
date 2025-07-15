# Data packages for Reproducible Examples

See https://github.com/splor-mg/datamart/issues/10#issuecomment-3075065559

- Frictionless 5.18.1 version installed with `pip install -r requirements.txt`.
- Need run `sudo apt-get install graphviz` on Ubuntu.
- To update `package_erd.png` file just run `python scripts.py` (python virtual env must be activated).
- To update `package_erd2.png` file just run `python scripts scripts_from_yaml.py`(python virtual env must be activated)
- The `python scripts.py` creates an ERD based on Frictionless Describe object, or infering datapackage from its data.
- The `python scripts scripts_from_yaml.py` creates an ERD on Frictionless Package object, or using `datapackage.yaml` alread created on the repo.