import sys

grades = [int(x) for x in sys.argv[1:]]
average = sum(grades) / len(grades)
best_grades = [g for g in grades if g > average]

print(best_grades)
