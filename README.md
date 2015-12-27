# PyDSA

[![Build Status](https://travis-ci.org/aktech/pydsa.svg?branch=master)](https://travis-ci.org/aktech/pydsa)
[![Join the chat at https://gitter.im/aktech/pydsa](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/aktech/pydsa?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Python Data Structure and Algorithms Library (α-mode)

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
$ git clone https://github.com/aktech/pydsa.git
```

You should then install the dependency for running the tests:

* [pytest](http://pytest.org/latest/getting-started.html#getstarted)

To run tests:

```
$ py.test
```

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/aktech/pydsa/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
