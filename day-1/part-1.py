import re
from sys import stdin

s = 0
for line in stdin:
    line = line.rstrip()
    digits = re.findall(r"\d", line)
    v = int(digits[0] + digits[-1])
    s += v
print(s)