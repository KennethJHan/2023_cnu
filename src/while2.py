result = 0
n = 1
while n < 11:
    result += n
    n += 1

print(result)

##########

result = 0
n = 1
while True:
    if n > 10:
        break

    result += n
    n += 1

print(result)
