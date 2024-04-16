height = float(input("Enter your heights: "))


if height > 3:
    raise ValueError("Human height is not over 3 meters")

weight = int(input("Please enter your weight: "))

bmi = weight/height ** 2

print(bmi)