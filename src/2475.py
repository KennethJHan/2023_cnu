sum_val = 0
for i in range(5):
    sum_val += int(input()) ** 2

res = sum_val % 10
print(res)
