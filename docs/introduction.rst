Introduction
============

Composability in Python
-----------------------

Composability is highly desirable in programming,
as it allows parts of a program to be reused and recombined,
and their behaviors to be easily reasoned about.

To write composable code, one usually employs
functional programming concepts, namely pure functions
and immutability.

The ease to which this can be done depends on the
built-in support in each programming language.

Python has sufficient built-in support for
functional programming for many practical purposes.
However, its syntax is riddled with quirks
that prevent effective composition.

Consider::

    from itertools import chain

    list(chain.from_iterable(map(
        lambda x: [x, x * 2],
        filter(
            lambda x: x % 2 == 0,
            map(lambda x: x + 1, range(10)),
        ),
    )))


Even though the above code is modular,
it is difficult to read.

Other alternatives also have flaws.
Comprehensions::

    list(chain.from_iterable(
        [x, x * 2] for x in (x + 1 for x in range(10)) if x % 2 == 0
    ))

are difficult to read when multiply nested,
while iterative solutions::

    acc = []

    for x in range(10):
        y = x + 1

        if y % 2 == 0:
            acc.extend([y, y * 2])

are not modular and error-prone.

This package presents a solution::

    from pysweet import Iterable_

    (
        Iterable_(range(10))
        .map(lambda x: x + 1)
        .filter(lambda x: x % 2 == 0)
        .flat_map(lambda x: [x, x * 2])
        .to_list()
    )
