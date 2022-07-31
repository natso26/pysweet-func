pysweet-func
============

|test| |codecov| |Documentation Status| |PyPI version|

Rationale
---------

Python can be unwieldy in real production systems, due to its favor of
imperative programming style. However, attempts to rewrite code to be
more modular in functional programming style usually result in
hard-to-read code due to Python’s quirky syntax in this area.

Consider the following example:

.. code:: python

   acc = []

   for x in range(10):
       y = x + 1

       if y % 2 == 0:
           acc.extend([y, y * 2])

In the imperative style, the code is clean and pythonic, but with more
business logic, the code can get complicated with nested for loops and
mutable accumulators.

To solve this, we may try to rewrite the code using comprehensions:

.. code:: python

   acc = [
       z for y in (x + 1 for x in range(10))
       for z in [y, y * 2] if y % 2 == 0
   ]

The result is unfortunately not very readable. When nested,
comprehensions can also get complicated.

Another alternative is functional Python:

.. code:: python

   from itertools import chain

   acc = list(chain.from_iterable(map(
       lambda x: [x, x * 2],
       filter(
           lambda x: x % 2 == 0,
           map(lambda x: x + 1, range(10)),
       ),
   )))

I favored this style for quite some time. Although it may look
unfamiliar at first, the code is modular and each part can easily be
reasoned about.

However, in e.g. JavaScript, the same logic is much easier to read:

.. code:: js

   acc = [...Array(10).keys()]
       .map(x => x + 1)
       .filter(x => x % 2 === 0)
       .flatMap(x => [x, x * 2])

So we can ask: can we write the same thing in Python? (Note: the
JavaScript version has worse performance in general due to eager
evaluation.)

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

Many other excellent functional programming libraries provide similar
capabilities to ``pysweet``. However, ``pysweet`` sets itself apart by
being incredibly lightweight: it is only light syntactic sugar over
built-in Python functionality. This has the advantages of:

-  Minimizing performance overhead;
-  Simplifying debugging;
-  Making developer onboarding easy and preventing solution lock-in.

Moreover, the library is very small, with less than 100 lines of code!

``pysweet`` is being successfully used in a production repo.

Python can become composable with a little sweetening from ``pysweet``.

Features
--------

Fluent iterable
~~~~~~~~~~~~~~~

Wrapper iterable implementing method chaining, in the style of
JavaScript and Scala.

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

Available in many modern languages, even systems ones such as Go.

.. code:: python

   from pysweet import block_

   val = lambda: block_(
       x := 1,
       x + 1,
   )
   # val() == 2

Statements as expressions
~~~~~~~~~~~~~~~~~~~~~~~~~

Composable control flow, as found in functional languages such as Scala
and Haskell.

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

Bonus: The ternary operator in its natural order :)

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
