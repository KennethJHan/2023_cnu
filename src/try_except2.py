try:
    num = int(input("Enter: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Check your input")

print("#END")
