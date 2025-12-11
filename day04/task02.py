from utils import Reader
import time
import numpy as np
from collections import deque

start = time.perf_counter()

name: str = "inputs/input04.0.txt"
input_file = Reader(name).read_txt_to_str()
input_file = input_file.split('\n')

y: int = 0
x: int = 0
rolls: int = 0
removed_rolls: deque[list[int]] = deque()
temp: int = 0

array_range: int = int(input("Array range [x * x]: "))

paper_shelf = np.zeros((array_range, array_range), dtype=int)

for line in input_file:
    for roll in line:
        match roll:
            case "@":
                paper_shelf[y][x] = 1

                if x < array_range - 1:
                    x += 1
                else:
                    y += 1
                    x = 0
            case ".":
                if x < array_range - 1:
                    x += 1
                else:
                    y += 1
                    x = 0
x = 0
y = 0



def check(_x: int, _y: int, _array_range) -> int:
    _nearby_rolls: int = 0
    check_y = y-1
    check_x = x-1
    while _y+1 >= check_y:
        while check_x <= _x+1:
            if (0 <= check_x < _array_range and 0 <= check_y < _array_range) and paper_shelf[check_y][check_x] == 1:
                _nearby_rolls += 1
            check_x += 1
        check_y += 1
        check_x = _x-1
    return _nearby_rolls-1

while True:
    for y in range(array_range):
        for x in range(array_range):
            if paper_shelf[y][x] == 1:
                temp = check(x, y, array_range)
                if temp < 4:
                    rolls += 1
                    removed_rolls.append([x, y])

    for _list in removed_rolls:
        paper_shelf[_list[1]][_list[0]] = 0

    if not removed_rolls:
        break

    removed_rolls.clear()

print(rolls)
end = time.perf_counter()
print(f"time: {end - start:.4f} sec")
