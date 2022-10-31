import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed)
print(x)

x = numpy.median(speed)
print(x)

x = stats.mode(speed, axis=0, keepdims=False)
for y in x:
    print(y)

speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

array = [33, 111, 138, 28, 59, 77, 97]

y = numpy.mean(array)
print(y)

print("\nPt fiecare valoarea diferenta fata de medie")
for z in array:
    print(str(z) + " - " + str(y) + " = " + str(z-y))

array2 = []

print("\nValoarea patrata pentru diferenta")
for z in array:
    array2.append(numpy.power(z-y, 2))
    print(str(z-y) + "^2" + " = " + str(array2[len(array2) - 1]))

print("\n\nMedia diferentelor patrate")
m = numpy.mean(array2)
print(m)

print("deviata standard")
speed = [32,111,138,28,59,77,97]
m = numpy.var(speed)
print(m)

print("abaterea standard")
m = numpy.std(speed)
print(m)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
m = numpy.percentile(ages, 75)
print("percentile")
print(m)

print("\n\n\n\nelemente aleatorii")
d = numpy.random.uniform(0.0, 5.0, 250)
for i in d:
    print(i)

