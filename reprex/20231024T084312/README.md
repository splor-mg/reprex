# Reprex

- Single quotes let you put almost any character in your string, and won't try to parse escape codes. `'\n'` would be returned as the string `\n`.
- Double quotes parse escape codes. `"\n"` would be returned as a line feed character.

Enclosing strings in double quotes allows you to use escapings to represent ASCII and Unicode characters.

```bash
$ pytest
========================================= test session starts ==========================================
platform darwin -- Python 3.11.2, pytest-7.4.2, pluggy-1.3.0
rootdir: /Users/fjunior/Projects/splor/reprex/reprex/20231024T084312
collected 2 items                                                                                      

test_quotes.py F.                                                                                [100%]

=============================================== FAILURES ===============================================
__________________________________________ test_single_quotes __________________________________________

    def test_single_quotes():
        resource = Resource('resource-single-quotes.yaml')
        report = resource.validate()
        logging.warning(report.tasks[0].errors[0].message)
>       assert report.valid
E       assert False
E        +  where False = {'valid': False,\n 'stats': {'tasks': 1, 'errors': 1, 'warnings': 0, 'seconds': 0.002},\n 'warnings': [],\n 'errors': [],...g',\n                        'tags': [],\n                        'note': '"delimiter" must be a 1-character string'}]}]}.valid

test_quotes.py:8: AssertionError
------------------------------------------ Captured log call -------------------------------------------
WARNING  root:test_quotes.py:7 The data source has not supported or has inconsistent contents: "delimiter" must be a 1-character string
======================================= short test summary info ========================================
FAILED test_quotes.py::test_single_quotes - assert False
===================================== 1 failed, 1 passed in 0.24s ======================================
```

## Links

- [syntax - YAML: Do I need quotes for strings in YAML? - Stack Overflow](https://stackoverflow.com/questions/19109912/yaml-do-i-need-quotes-for-strings-in-yaml)
- [Encourage double quotes · Issue #155 · adrienverge/yamllint](https://github.com/adrienverge/yamllint/issues/155)