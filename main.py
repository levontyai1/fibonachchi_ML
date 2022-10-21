a = 1
b = 1
n = int(input()) - 2
i = 0

while i < n:
    c = a + b
    a = b
    b = c
    i = i + 1

print(b)
