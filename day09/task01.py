from utils import Reader
from collections import deque
import time

start = time.perf_counter()

name: str = "inputs/input09.0.txt"
input_file = Reader(name).read_txt_to_str()
input_file = input_file.split('\n')

x: int = 0
y: int = 0
temp_x: int = 0
temp_y: int = 0
a: int = 0
b: int = 0
rectangles: deque[int] = deque([0,0,0])
l_rectangles: int = 0
temp: int = 0

for line in input_file:
    line = line.split(',')
    x = int(line[0])
    y = int(line[1])
    for _line in input_file:
        _line = _line.split(',')
        if _line[0] != line[0] or _line[1] != line[1]:
            temp_x = int(_line[0])
            temp_y = int(_line[1])

            a = x - temp_x
            b = y - temp_y

            if a == 0 or b == 0:
                continue
            if a < 0:
                a = a * -1
            if b < 0:
                b = b * -1

            a = a + 1
            b = b + 1

            temp = a * b

            if temp > l_rectangles:
                l_rectangles = temp



print(l_rectangles)

end = time.perf_counter()
print(f"time: {end - start:.4f} sec")