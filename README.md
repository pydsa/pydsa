# PyDSA

[![Build Status](https://travis-ci.org/pydsa/pydsa.svg?branch=master)](https://travis-ci.org/aktech/pydsa)
[![Join the chat at https://gitter.im/pydsa/pydsa](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/pydsa/pydsa?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Documentation Status](https://readthedocs.org/projects/pydsa/badge/?version=latest)](http://pydsa.readthedocs.org/en/latest/?badge=latest)

Mailing List: https://groups.google.com/forum/#!forum/pydsa

Python Data Structure and Algorithms Library (α-mode)

1. [Installation](#installation)
2. [Usage](#usage)
3. [Development Environment](#development-environment)
4. [Contributing](#contributing)

## Installation

To install PyDSA, simply run:

```shell
$ python setup.py install
```

## Usage

```python
In [1]: from pydsa import quick_sort

In [2]: a = [2, 10, 10, 2, 7, 7, 2, 5, 4, 10]

In [3]: quick_sort(a)
Out[3]: [2, 2, 2, 4, 5, 7, 7, 10, 10, 10]
```

```python
In [1]: from pydsa import merge_sort

In [2]: b = [5, 1, 2, 3, 4, 3, 9, 7, 8, 5]

In [3]: merge_sort(b)
Out[3]: [1, 2, 3, 3, 4, 5, 5, 7, 8, 9]

```

## Development Environment

The source code is managed with the Git version control system. To get the latest development version and access to the full repository, clone the repository from Github with:

```
$ git clone https://github.com/pydsa/pydsa.git
```

You should then install the development requirements:

```shell
$ pip install -r requirements-dev.txt
```

To run tests:

```
$ py.test
```

## Contributing

There are multiple ways you can contribute to PyDSA. For example, you can:

* Add missing documentation.
* Add/improve efficiency of algorithms or data structures.
* Report bugs.
* Request/submit new algorithms.

Please use Github's pull request/issues feature for all contributions and take a look at the [PyDSA wiki](https://github.com/pydsa/pydsa/wiki).

**Wiki Quick Links**  

* [Contributing to PyDSA](https://github.com/pydsa/pydsa/wiki/Contributing-to-PyDSA)
* [Writing and Running Tests in PyDSA](https://github.com/pydsa/pydsa/wiki/Writing-and-Running-Tests-in-PyDSA)
* [Project Ideas](https://github.com/pydsa/pydsa/wiki/Project-Ideas)
* [RGSoC 2016 Student Instructions](https://github.com/pydsa/pydsa/wiki/RGSoC-2016-Student-Instructions)
