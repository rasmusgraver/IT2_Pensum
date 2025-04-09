
a = 0
b = 1
for i in range(1, 6):
  if a > b:
    b = a
  else:
    a += 1
  # print(i, a, b)

print(b) 

"""
Løkken og verdiene blir:
i   a   b 
0   0   1
1   1   1 
2   2   1 
3   2   2
4   3   2
5   3   3
"""