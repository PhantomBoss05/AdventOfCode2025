from utils import Reader                                                                                                #DepthFirstSearch: https://www.youtube.com/watch?v=iaBEKo5sM7w
import time

start = time.perf_counter()

name: str = "inputs/input11.0.txt"
input_file = Reader(name).read_txt_to_str()
my_paths: list
counter: int = 0

def create_dict(_input: str)-> dict:
    devices = {}

    _input = _input.split('\n')

    for line in _input:
        line = line.split(':')
        devices[line[0].strip()] = line[1].split()
    return devices

def paths(dictionary: dict, start: str, goal: str)-> list:
    all_paths = []

    def depth_first_search(node, path):
        if node == goal:
            all_paths.append(path[:])
            return
        for _next in dictionary.get(node, []):
            if _next in path:
                continue
            path.append(_next)
            depth_first_search(_next, path)
            path.pop()

    depth_first_search(start, [start])
    return all_paths


reactor_paths = create_dict(input_file)

my_paths = paths(reactor_paths, "svr", "out")

for p in my_paths:
    if "fft" in p and "dac" in p:
        counter += 1
    print(" -> ".join(p))
print(f"Out of {len(my_paths)} paths there are {counter} valid paths")
end = time.perf_counter()
print(f"time: {end - start:.4f} sec")