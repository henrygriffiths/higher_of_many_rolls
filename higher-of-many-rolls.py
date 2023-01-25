import random

number_of_sides  =  int(input("How many sides on your dice? "))
number_of_rolls  =  int(input("How many rolls of your dice? "))

sum_of_results = 0.0

trials = 0
while trials < 10**6:
    sum_of_results += max([int(random.random() * number_of_sides) + 1 for _ in range(number_of_rolls)])
    trials += 1

print("Average result of rolling {1} times and taking the highest is about {0}".format(sum_of_results/trials, number_of_rolls))



