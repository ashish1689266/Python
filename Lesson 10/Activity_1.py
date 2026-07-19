# input an integer value
n = int(input("Enter the number whose sum you want to find: "))
sum = 0

# Iterates for n+1 times: i = 1 to n+1
for val in range(1, n + 1, 1):
    sum = sum + val

print("\nSum =", sum)
