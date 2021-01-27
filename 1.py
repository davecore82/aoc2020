#!/usr/bin/python3

with open("1.data") as f:
    numbers = [int(x) for x in f.read().split()]

for i, number in enumerate(numbers):
    complementary = 2020 - int(number)
    if complementary in numbers[i+1:]:
        print("Solution Found: {} and {} with a product of {}".format(number, complementary, number * complementary))
        break
