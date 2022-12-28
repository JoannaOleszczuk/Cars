cars = []
while True:
    CarBrand = input("Type the car brand. To end the application please type END ")
    if CarBrand == "END":
        break
    CarColor = input("Type the car color. ")
    ListElement = [CarBrand, CarColor]
    cars.append(ListElement)

i = 0
for element in cars:
    i = i + 1
    print("Car brand number " + str(i) + " is: " + element[1] + " " + element[0])

