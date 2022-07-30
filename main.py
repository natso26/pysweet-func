from itertools import chain

list(chain.from_iterable(map(
    lambda x: [x, x * 2],
    filter(
        lambda x: x % 2 == 0,
        map(lambda x: x + 1, range(10)),
    ),
)))

print(x)

list(chain.from_iterable(
    [x, x * 2] for x in (x + 1 for x in range(10)) if x % 2 == 0
))

print(x)

acc = []

for x in range(10):
    y = x + 1

    if y % 2 == 0:
        acc.extend([y, y * 2])

print(x)

from pysweet import Iterable_

(
    Iterable_(range(10))
    .map(lambda x: x + 1)
    .filter(lambda x: x % 2 == 0)
    .flat_map(lambda x: [x, x * 2])
    .to_list()
)

print(x)
