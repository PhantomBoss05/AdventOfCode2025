from utils import Reader
import time
from collections import deque
from math import prod

start = time.perf_counter()

name: str = "inputs/input06.0.txt"
input_file = Reader(name).read_txt_to_str()
input_file = input_file.split('\n')
count_dequeues: int = 0
operation: str = "\0"
result: int = 0
task: deque[int] = deque()

dequeues = {i: deque() for i in range(len(input_file))}

for key in dequeues:
    dequeues[key].extend(input_file[key].split())

count_dequeues = len(dequeues)

for i in range(len(dequeues[0])):
    operation = dequeues[len(dequeues)-1][i]
    match operation:
        case "*":
            for n in range(len(dequeues)-1):
                task.append(int(dequeues[n][i]))
            result += prod(task)
            task.clear()
        case "+":
            for n in range(len(dequeues) - 1):
                task.append(int(dequeues[n][i]))
            result += sum(task)
            task.clear()

print(result)
end = time.perf_counter()
print(f"time: {end - start:.4f} sec")