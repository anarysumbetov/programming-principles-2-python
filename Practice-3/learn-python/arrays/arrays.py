cars = ["Ford", "Volvo", "BMW"]
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"
x = cars[0]
print(x)
cars[0] = "Toyota"
print(cars[0])
print(len(cars))
for z in cars:
    print(z)
cars.append("Honda")
cars.pop(1)
print(cars)
cars.remove("BMW")
print(cars)