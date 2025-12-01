from utils import Reader
from collections import deque
import time

start = time.perf_counter()

name: str = "inputs/input1.0"
input_file = Reader(name).read_txt_to_str()
input_file = input_file.replace('R', '')
input_file = input_file.replace('L', '-')
input_file = input_file.split("\n")

rotation: deque[int] = deque(range(0, 100))
password: int = 0

rotation.rotate(50)

for line in input_file:
    amount = int(line)
    password += abs(amount) // 100
    if amount > 0:
        amount %= 100
        rotated_values = list(rotation)[1: amount+1]
    else:
        amount = -100 + amount % 100
        rotated_values = list(rotation)[amount: 101]
    rotation.rotate(-int(line))

    password += rotated_values.count(0)

print(password) #2529

end = time.perf_counter()
print(f"time: {end - start:.4f} sec")