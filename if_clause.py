name = "Windel"
height_meter = 2
weight_kg = 90

BMI = weight_kg / (height_meter ** 2)
print("BMI:")
print(BMI)

if BMI < 25:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")
