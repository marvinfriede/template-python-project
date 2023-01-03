# Template for open-source Python projects

![Python versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)
![Tests](https://github.com/marvinfriede/python-project/actions/workflows/test.yml/badge.svg)
[![codecov](https://codecov.io/gh/marvinfriede/python-project/branch/master/graph/badge.svg?token=UEKDZY459S)](https://codecov.io/gh/marvinfriede/python-project)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/marvinfriede/python-project/master.svg)](https://results.pre-commit.ci/latest/github/marvinfriede/python-project/master)
[![code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repository aims to provide a starting template for Python projects containing the most important configuration files
(which have to be tailored for your project!) and an initial directory structure separating source code and tests.

I tried to incorporate most "best practices" but in the end, most of the design choices and tools are just personal preferences.

The following tools are used: black, covdefaults, coverage, pre-commit, pylint, pytest, tox

<br>

## Source code

All of the source code goes into the [src/\<project-name\>](src/squarer) directory. Here, some _dunder_ files can be found:

- [\_\_version\_\_.py](src/squarer/__version__.py): just the version number as string, used by config files
- [\_\_init\_\_.py](src/squarer/__init__.py): entry point for program/library
- [\_\_main\_\_.py](src/squarer/__main__.py): same as `__init__.py` allowing calls via `python -m <prog>`

<br>

## Tests (pytest/tox)

Testing is done with `pytest` and `tox`. All tests go into the [test](test/) directory. Pytest automatically finds all directories
and modules as well as functions and classes within these matching `test_*.py`/`*_test.py` files, `Test*` classes, and `test_*`
functions and methods (automatic test discovery).

The [conftest.py](test/conftest.py) file is sort of a setup file that can be used to create additional configurations/hooks
([small example](https://github.com/tbmalt/tbmalt/blob/main/tests/conftest.py)) and setup code (fixtures) for all tests.

The test environment for pytest is setup with the `setup.cfg` and/or `pyproject.toml` file. `tox` needs extra configuration
which can be found in the _deps_ section of [tox.ini](tox.ini). Some projects also use a `requirements-tests.txt` file that lists
all test dependencies and is also given in the _deps_ section with `deps = -rrequirements-tests.txt`.
Furthermore, to run pytest from tox, the `commands` section must be given. Here, additional options for the code coverage report
from the `coverage` tool are given.

<br>

_When to use pytest, coverage and tox?_

Personally, I mostly use just pytest without coverage to test in my working environment with `pytest -svv test` or a specific
test module. Before committing, however, it is a good idea to check if your code also runs in different environments, which is where
`tox` comes in. Running just `tox`, will test in all environments specified in [tox.ini](tox.ini)'s envlist and may take some
time. Certain environments can be selected with `tox -e py37`. Note that `tox` must be able to find a Python interpreter for
each version given in the envlist.

<details>
<summary>How to provide the Python interpreters for tox.</summary>

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
- expected fails: testing if the code handles wrong inputs (`with pytest.raises(Exception): ...` or `@pytest.mark.xfail`)
- check for [test pollution](https://github.com/asottile/detect-test-pollution) by randomizing the order of tests ([pytest-plugin](https://pypi.org/project/pytest-random-order/))

<br>

## Setup files and Packaging

Packaging is done with [`setuptools`](https://setuptools.pypa.io/en/latest/index.html), which is configured through the `pyproject.toml` and/or `setup.cfg`/`setup.py` files.

<details>
<summary>
  <code>pyproject.toml</code> vs.
  <code>setup.cfg</code> vs
  <code>setup.py</code>
</summary>

The `setup.py` file is a Python script and configuration is passed through keyword arguments of `setuptools.setup()`. This is not recommended due to possible security and parsing issues. The same setup can be accomplished in a declarative style within `setup.cfg` and `setup.py` remains mostly empty only calling `setuptools.setup()`.
The `pyproject.toml` file aims to unify configuration files including various tools like black or pytest. For packaging, it is very similar to `setup.cfg`. However, `pyproject.toml` has not been adopted as the default yet and many projects still use `setup.cfg` to declare the packaging setup. Note that `setup.py` is not necessary if a `pyproject.toml` is present.

</details>

#### `pyproject.toml`

- minimal build specification to use with setuptools
- configuration of other tools (black, pytest, mypy, ...)

[](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html#using-a-src-layout)

#### `setup.cfg`

- declarative configuration for setuptools
- [_metadata_](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html#metadata): must at least contain _name_ and _version_
- [_options_](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html#options): package discovery, dependencies
  - [additional setup](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html#using-a-src-layout) required for `src/` layout
- [_options.extras_require_](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies): optional dependencies (dev tools, docs, ...)
- [_options.package_data_](https://setuptools.pypa.io/en/latest/userguide/datafiles.html#package-data): inclusion of other, non-Python files (marker files, data, ...)
  - alternative: `MANIFEST.in`
- [_options.entry_points_](https://setuptools.pypa.io/en/latest/userguide/entry_point.html): entry point for command line interface
- can also hold configuration of other tools

<br>

The package can be installed with `pip install .` or something like `pip install .[dev]` to also install additional dependencies specified in `setup.cfg`'s _options.extras_require_. Pass the `-e` flag for editable mode, which loads the package from the source directory, i.e., changing the source code does not require a new installation.

<br>

## CI - Continuous Integration (with GitHub Actions)

**Important!** CI in private repositories is generally limited (to _x_ minutes of execution time).

...

<br>

## More

Tools
- [pre-commit.ci](https://github.com/apps/pre-commit-ci/)
- [codecov](https://github.com/apps/codecov/)

Websites
- [create .gitignore](https://www.toptal.com/developers/gitignore)
- [choose license](https://choosealicense.com/)
