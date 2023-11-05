for value in range(1, 6):
    print(value)
    # on passing third argumenet in range ia adds that value when generating numbers.
    odd_numbers = list(range(2, 11, 1))
    print(odd_numbers)

squares = []
for value in range(1, 11):
    # square = value ** 2
    squares.append(value ** 2)
    # squares.append(square)

print(squares)

squares = [value ** 2 for value in range(1, 11)]
print(squares)

for numbers in range(1, 20):
    print(numbers)

for numberss in range(1,1000000):
    print(numberss)
min(numberss)
max(numberss)