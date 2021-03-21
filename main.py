###solution to exercise 69 from ben stephenson's "the python workbook".

p = 3

for i in range(1,16):
  if i == 1:
    print(p)
  else:
    k = i - 1
    p += (4 * (-1) ** i) / ((k * 2) * (k * 2 + 1) * (k * 2 + 2))
    print(p)
