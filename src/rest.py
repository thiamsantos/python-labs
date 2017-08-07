from typing import Tuple

def add(*args: Tuple[int]) -> int:
    accumulator = 0

    for i in args:
        accumulator += i

    return accumulator

print(add(1,2,3))
