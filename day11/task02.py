from utils import Reader                                                                                                #DepthFirstSearch: https://www.youtube.com/watch?v=iaBEKo5sM7w
import time

start = time.perf_counter()

name: str = "inputs/input11.0.txt"
input_file = Reader(name).read_txt_to_str()
my_paths: list
counter: int = 0
path_direction_dac_fft: bool = True

def create_dict(_input: str)-> dict:
    devices = {}

    _input = _input.split('\n')

    for line in _input:
        line = line.split(':')
        devices[line[0].strip()] = line[1].split()
    return devices

def paths(dictionary: dict, start: str, goal: str)-> int:
    count: int = 0

    def depth_first_search(node, path):
        nonlocal count
        if node == goal:
            count += 1
            return
        for _next in dictionary.get(node, []):
            if _next in path:
                continue
            path.append(_next)
            depth_first_search(_next, path)
            path.pop()

    depth_first_search(start, [start])
    return count


reactor_paths = create_dict(input_file)

if paths(reactor_paths, "dac", "fft") > 0:
    print("dac -> fft")

    counter += paths(reactor_paths, "svr", "dac")
    counter *= paths(reactor_paths, "dac", "fft")
    counter *= paths(reactor_paths, "fft", "out")
else:
    print("fft -> dac")
    counter += paths(reactor_paths, "svr", "fft")
    counter *= paths(reactor_paths, "fft", "dac")
    counter *= paths(reactor_paths, "dac", "out")

print(counter)
end = time.perf_counter()
print(f"time: {end - start:.4f} sec")
