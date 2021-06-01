
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

# Exercise 1

# assigning numbers to start from 0 to 20
numbers = np.arange(0, 20)
print(numbers)

# the average/middle number
mean = np.mean(numbers)
print(mean)

# Standard deviation measures the amount of values
std = np.std(numbers)
print(std)

# Variance measures how spread out the data is
var = np.var(numbers)
print(numbers)

# Exercise 2

# categories and data
nums = [0.5, 0.7, 1, 1.2, 1.3, 2.1]
bins = [0, 1, 2, 3, 4]

# printing categories and formation of the data
print("nums: {}".format(nums))
print("bins: {}".format(bins))
print("Result: {}".format(histogram(nums, bins)))

# plotting type of graph, the x and y axis labels, the title of the graph and action that it should show.
plt.hist(nums, bins)
plt.xlabel("Nums")
plt.ylabel("Bins")
plt.title("Histogram of nums against bins.")
plt.show()
