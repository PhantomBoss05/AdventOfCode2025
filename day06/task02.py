from utils import Reader
import time
from collections import deque
from math import prod

start = time.perf_counter()

name: str = "inputs/input06.0.txt"
input_file = Reader(name).read_txt_to_str()
input_file = input_file.split('\n')

dequeues = {}
count_ws: int = 0
i: int = 0
operation: str = "\0"
result: int = 0
operators: deque[str] = deque()
temp_task: deque[int] = deque()

for o in input_file[len(input_file) - 1]:
    if o != '+' and o != '*':
        count_ws += 1
    elif count_ws > 0:
        dq = deque()
        for n in range(len(input_file) - 1):
            dq.append(input_file[n][:count_ws])
            input_file[n] = input_file[n][count_ws+1:]
        count_ws = 0
        dequeues[i] = dq
        i += 1

if count_ws > 0:
    dq = deque()
    count_ws += 1
    for n in range(len(input_file) - 1):
        dq.append(input_file[n][:count_ws])
        input_file[n] = input_file[n].replace(input_file[n][:count_ws + 1], '')
    count_ws = 0
    dequeues[i] = dq

def cephalopod(column: deque) -> deque[int]:
    task: deque[int] = deque()
    temp: str = ""
    for value in range(len(column[0])):
        for j in range(len(column)):
            temp += column[j][value]
        temp = temp.replace(' ', '')
        if temp == "":
            temp = "0"
        task.append(int(temp))
        temp = ""

    return task

input_file = input_file[-1].split()
operators.extend(input_file)
for i in range(len(input_file)):
    operation = operators.popleft()
    match operation:
        case "*":
            temp_task = cephalopod(dequeues[i])
            try:
                temp_task.remove(0)
            except ValueError:
                pass
            result += prod(temp_task)
        case "+":
            result += sum(cephalopod(dequeues[i]))
print(result)
end = time.perf_counter()
print(f"time: {end - start:.4f} sec")