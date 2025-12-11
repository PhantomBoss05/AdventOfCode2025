from utils import Reader
import time

start = time.perf_counter()

name: str = "inputs/input02.0.txt"
input_file = Reader(name).read_txt_to_str()
temp: list = []
rangeStart: str = "\0"
rangeEnd: str = "\0"
part1: str = "\0"
part2: str = "\0"
invalidIDs: list = []

input_file = input_file.split(',')

for idRange in input_file:
    temp = idRange.split('-')
    rangeStart = temp[0]
    rangeEnd = temp[1]

    while int(rangeStart) <= int(rangeEnd):
        if (int(rangeStart) % 10 >= 1 or int(rangeStart) % 10 == 0) and (len(rangeStart) % 2 == 0):                     #checks if rangeStart is greater than 9 and if length form rangeStart is even
            part1 = rangeStart[:len(rangeStart)//2]                                                                     #splits the digit in half
            part2 = rangeStart[len(rangeStart)//2:]

            if part1 == part2:                                                                                          #checks if both parts are even
                invalidIDs.append(rangeStart)
        rangeStart = str(int(rangeStart) + 1)




print(sum(map(int, invalidIDs)))
end = time.perf_counter()
print(f"time: {end - start:.4f} sec")