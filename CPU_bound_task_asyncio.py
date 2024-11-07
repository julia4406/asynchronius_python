# find all integer divisors for a given numbers
# ex.:  10: (1, 2, 5, 10)
#       17: (1, 17)
#       35: (1, 5, 7, 35)
#       100: (1, 2, 4, 5, 10, 20, 25, 50, 100)

import time
from typing import Sequence, Tuple
import asyncio

SequenceInt = Sequence[int]
TupleIntoDivisors = Tuple[int, ...]

numbers = (
    3_111_000, 3_111_001, 1_111_111, 2_222_222, 8_888_888, 2_456_789,
    8_654_321, 1_000_000, 7_777_777, 2_123_098, 5_000_000, 7_000_111,
    8_001_123, 2_111_001, 9_010_801, 3_331_634, 1_999_123, 4_098_123,
    7_360_109, 8_012_364, 1_000_001, 2_000_000, 3_333_333, 7_098_765,
    9_000_001, 7_001_999, 8_888_005, 2_010_222, 6_209_245, 5_555_032,
)


async def async_factorize_single(number: int) -> TupleIntoDivisors:
    """ return tuple of divisors for one select number"""
    return tuple(x for x in range(1, number + 1) if number % x == 0)


async def async_factorize_single_print(index: int, number: int) -> None:
    print(f"Start task: {index}")
    dividers = await async_factorize_single(number)
    print(f"Result for task {index}: factorize_single({number}) = {dividers}")
    print("*" * 50)


async def main_async(in_numbers: SequenceInt) -> None:
    async with asyncio.TaskGroup() as tg:
        [tg.create_task(async_factorize_single_print(index, number))
         for index, number in enumerate(in_numbers)]



if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main_async(numbers))
    main_async_duration = time.perf_counter() - start
    print(main_async_duration)