pysweet-func
============

|test| |codecov| |Documentation Status| |PyPI version|

Why ``pysweet``?
----------------

Python can sometimes be unwieldy in production.

Consider the following 3 variants
of the same logic:

.. code:: python

   acc = []

   for x in range(10):
       y = x + 1

       if y % 2 == 0:
           acc.extend([y, y * 2])

.. code:: python

   acc = [
       z for y in (x + 1 for x in range(10))
       for z in [y, y * 2] if y % 2 == 0
   ]

.. code:: python

   from itertools import chain

   acc = list(chain.from_iterable(map(
       lambda x: [x, x * 2],
       filter(
           lambda x: x % 2 == 0,
           map(lambda x: x + 1, range(10)),
       ),
   )))

* The first is in the imperative style;
  it can become convoluted as requirements evolve.

* The second uses comprehensions,
  which can get complicated when nested.

* The last utilizes functional programming:
  more modular, but not as readable.

In JavaScript, the same logic is simpler:

.. code:: js

   acc = [...Array(10).keys()]
       .map(x => x + 1)
       .filter(x => x % 2 === 0)
       .flatMap(x => [x, x * 2])

Can we write analogous code in Python?

Now you can with ``pysweet``:

.. code:: python

   from pysweet import Iterable_

   acc = (
       Iterable_(range(10))
       .map(lambda x: x + 1)
       .filter(lambda x: x % 2 == 0)
       .flat_map(lambda x: [x, x * 2])
       .to_list()
   )

Compared to many excellent alternatives,
``pysweet`` is lightweight
with around 100 lines of code.

Being only syntactic sugar, ``pysweet``:

* has little performance overhead;
* does not complicate debugging;
* makes onboarding new developers easy.

``pysweet`` has successfully been used in production.

Sweeten Python with ``pysweet``!

Features
--------

Fluent iterable
~~~~~~~~~~~~~~~

Iterable with method chaining
in the style of JavaScript and Scala.

.. code:: python

   from pysweet import Iterable_

   (
       Iterable_([1, 2])
       .map(lambda x: x + 1)
       .to_list()
   )
   # [2, 3]

Multi-expression lambda
~~~~~~~~~~~~~~~~~~~~~~~

As in many modern languages,
even a systems one like Go.

.. code:: python

   from pysweet import block_

   val = lambda: block_(
       x := 1,
       x + 1,
   )
   # val() == 2

Statements as expressions
~~~~~~~~~~~~~~~~~~~~~~~~~

Composable control flow as in functional languages
such as Scala and Haskell.

Bonus: ``if_`` is the ternary operator
in the natural order.

.. code:: python

   from pysweet import if_, try_, raise_

   if_(
       True,
       lambda: 1,
       lambda: 2,
   )
   # 1

   try_(
       lambda: raise_(Exception('test')),
       catch=lambda e: str(e),
   )
   # 'test'

Documentation
-------------

-  `Read the Docs <https://pysweet-func.readthedocs.io>`__

Installation
------------

-  `PyPI <https://pypi.org/project/pysweet-func>`__

.. |test| image:: https://github.com/natso26/pysweet-func/actions/workflows/test.yml/badge.svg?branch=main&event=push
.. |codecov| image:: https://codecov.io/gh/natso26/pysweet-func/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/natso26/pysweet-func
.. |Documentation Status| image:: https://readthedocs.org/projects/pysweet-func/badge/?version=latest
   :target: https://pysweet-func.readthedocs.io/en/latest/?badge=latest
.. |PyPI version| image:: https://badge.fury.io/py/pysweet-func.svg
   :target: https://badge.fury.io/py/pysweet-func
