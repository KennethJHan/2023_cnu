relative_value = [7.8, -5.4, 3.2, -11.8]

relative_value.sort(key=abs)
print(relative_value)

relative_value.sort(key=abs, reverse=True)
print(relative_value)
