pysweet-func
============

|test| |codecov| |Documentation Status| |PyPI version|

Why ``pysweet``?
----------------

Consider the following variants
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

* The imperative style
  can grow complex as requirements evolve;

* The comprehension style
  can get complicated when nested;

* The functional style
  is not very readable in Python.

In JavaScript, the same logic can be written:

.. code:: js

   acc = [...Array(10).keys()]
       .map(x => x + 1)
       .filter(x => x % 2 === 0)
       .flatMap(x => [x, x * 2])

Can we write analogous code in Python?

Now you can with ``pysweet``!

.. code:: python

   from pysweet import Iterable_

   acc = (
       Iterable_(range(10))
       .map(lambda x: x + 1)
       .filter(lambda x: x % 2 == 0)
       .flat_map(lambda x: [x, x * 2])
       .to_list()
   )

``pysweet`` also offers many other similar features.

``pysweet`` is:

* lightweight, with around 100 lines of code;

* mostly syntactic sugar, so it is
  performant, easy to debug, and easy to learn;

* successfully used in production.

Sweeten Python with ``pysweet``!

Sample features
---------------

* Iterable with method chaining,
  in the spirit of JavaScript and Scala:

.. code:: python

   from pysweet import Iterable_

   (
       Iterable_([1, 2])
       .map(lambda x: x + 1)
       .to_list()
   )
   # [2, 3]

* Multi-expression lambda,
  common in modern languages:

.. code:: python

   from pysweet import block_

   val = lambda: block_(
       x := 1,
       x + 1,
   )
   # val() == 2

* Statement as expression,
  in the spirit of Scala and Haskell
  (``if_`` is also the ternary operator):

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

Next steps
----------

-  `Installation <https://pypi.org/project/pysweet-func>`__
-  `Documentation <https://pysweet-func.readthedocs.io>`__

.. |test| image:: https://github.com/natso26/pysweet-func/actions/workflows/test.yml/badge.svg?branch=main&event=push
.. |codecov| image:: https://codecov.io/gh/natso26/pysweet-func/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/natso26/pysweet-func
.. |Documentation Status| image:: https://readthedocs.org/projects/pysweet-func/badge/?version=latest
   :target: https://pysweet-func.readthedocs.io/en/latest/?badge=latest
.. |PyPI version| image:: https://badge.fury.io/py/pysweet-func.svg
   :target: https://badge.fury.io/py/pysweet-func
