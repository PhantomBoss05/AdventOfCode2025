from utils import Reader
from collections import deque
import time

start = time.perf_counter()

name: str = "inputs/input01.0.txt"
input_file = Reader(name).read_txt_to_str()
input_file = input_file.replace('R', '')
input_file = input_file.replace('L', '-')
input_file = input_file.split("\n")

rotation: deque[int] = deque(range(0, 100))                                                                             #creates a deque from 0 to 99
password: int = 0

rotation.rotate(50)                                                                                                     #rotates the deque 50 digits

for line in input_file:
    rotation.rotate(-int(line))                                                                                         #rotates the deque

    if rotation[0] == 0:
        password += 1

print(password)

end = time.perf_counter()
print(f"time: {end - start:.4f} sec")