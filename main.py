number = input("Enter number:")
ko = 0
sum = 0
for diget in number:
       ko = ko + 1
       sum = (int(diget)) + sum
       main = sum / ko
       numbers_max = max(number)
       numbers_min = min(number)
print("Total:", sum)
print("Amount of numbers:", ko)
print("Arithmetic mean:", main)
print("numbers_max:", numbers_max)
print("numbers_min:", numbers_min)