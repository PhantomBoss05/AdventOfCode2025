from utils import Reader
from collections import deque
import time

start = time.perf_counter()

name: str = "inputs/input11.0.txt"
input_file = Reader(name).read_txt_to_str()
input_file = input_file.replace(':', '')
input_file = input_file.split('\n')

devices: deque[str] = deque()
count_paths: int = 1

devices.append("you")

while devices:
    for line in input_file:
        line = line.split(' ')
        if devices[0] == "out":
            devices.popleft()
            break
        if line[0] == devices[0]:
            for i in range(1, len(line)):
                devices.append(line[i])
            count_paths += len(line)-2
            devices.popleft()
            break

print(count_paths)

end = time.perf_counter()
print(f"time: {end - start:.4f} sec")
