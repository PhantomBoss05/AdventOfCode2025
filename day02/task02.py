from utils import Reader
from sympy import divisors
from collections import deque
import time

start = time.perf_counter()

name: str = "inputs/input02.0.txt"
input_file = Reader(name).read_txt_to_str()

rangeStart: str = "\0"
rangeEnd: str = "\0"
all_divisors: deque = deque()
string_parts: deque = deque()
divisor: int = 0
i: int = 0
counter: int = 0

input_file = input_file.split(',')

for idRange in input_file:
    temp = idRange.split('-')
    rangeStart = temp[0]
    rangeEnd = temp[1]

    for n in range(int(rangeStart), int(rangeEnd)+1):
        all_divisors = divisors(len(str(n)))
        all_divisors.pop()
        while True:
            if len(str(n)) == 1:
                break
            divisor = all_divisors.pop()
            for i in range(0, len(str(n)), divisor):
                string_parts.append(str(n)[i:i+divisor])

            if string_parts.count(string_parts[0]) == len(string_parts):
                counter += n
                all_divisors.clear()
            #     print(f"The elements in {string_parts} are equal")
            # else:
            #     print(f"The elements in {string_parts} are not equal")
            string_parts.clear()

            if not all_divisors:
                break

print(counter)
end = time.perf_counter()
print(f"time: {end - start:.4f} sec")






