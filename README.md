# Template for open-source Python projects

This repository aims to provide a starting template for Python projects containing the most important configuration files
(which have to be tailored for your project!) and an initial directory structure separating source code and tests.

I tried to incorporate most "best practices" but in the end, most of the design choices and tools are just personal preferences.

<br>

## Source code

All of the source code goes into the [src/\<project-name\>](src/squarer) directory. Here, some *dunder* files can be found:
 - [\_\_version\_\_.py](src/squarer/__version__.py): just the version number as string, used by config files
 - [\_\_init\_\_.py](src/squarer/__init__.py): entry point for the command line interface
 - [\_\_main\_\_.py](src/squarer/__main__.py): same as `__init__.py` allowing calls via `python -m <prog>`

<br>

## Tests (pytest/tox)

Testing is done with `pytest` and `tox`. All tests go into the [test](test/) directory. Pytest automatically finds all directories
and modules as well as functions and classes within these starting with `test` (automatic test discovery).

The [conftest.py](test/conftest.py) file is sort of a setup file that can be used to create additional configurations/hooks
([small example](https://github.com/tbmalt/tbmalt/blob/main/tests/conftest.py)) and setup code (fixtures) for all tests.

The [requirements-tests.txt](test/requirements-tests.txt) file is not required by pytest but tox for setting up
the test environment as specified in tox's config file [tox.ini](tox.ini). Furthermore, to run pytest from tox, the `commands`
section must be given. Here, additional options for the code coverage report from the `pytest-cov` plugin are given.

<br>

*When to use pytest, coverage and tox?*

Personally, I mostly use just pytest without coverage to test in my working environment with `pytest -svv test` or a specific
test module. Before committing, however, it is a good idea if your code also runs in different environments, which is where
tox comes in. Running just `tox`, will test in all environments specified in the [tox.ini](tox.ini)'s envlist and may take some
time. Certain environments can be selected with `tox -e py37`. Note that the tox must be able to find a Python interpreter for
each version given in the envlist

<details><summary>How to provide the Python interpreters for tox.</summary>

Unfortunately, this does not directly work with something like a conda environment but you can setup the environments and provide
a symlink to a directory which is in your path.

```console
mamba create --name "py311" python=3.11 -y
ln -s /opt/miniforge3/envs/py311/bin/python3.11 ~/bin/python3.11
```

</details>

<br>

Finally, some handy features of pytest you should be aware of:
 - fixtures: common setup for multiple tests (e.g., reading file or database connection)
 - parametrize: multiple test cases for single function
 - expected fails: testing if the code handles wrong inputs (`pytest.raises(Exception)` or `@pytest.mark.xfail`)

 <br>

## Setup files and Packaging

...

<br>

## CI - Continuous Integration (with GitHub Actions)

**Important!** CI in private repositories is generally limited (to x minutes of execution time).

...
