def category_bmi(BMI):
    if (BMI < 16):
        return "Severely Underweight"
    elif (BMI>=16 and BMI < 18.5):
        return "Underweight"
    elif (BMI>=18.5 and BMI < 24.9):
        return "Healthy"
    elif (BMI>=25 and BMI <= 29.9):
        return "Overweight"
    elif (BMI >= 30):
        return "Obese"
       
def main():
    print(" Welcome to BMI Calculator!! ")
    try:
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))

        if weight<=0 or height<=0 :
            print("Weight and Height must be positive values.")
            return
        BMI= weight/(height**2)
        category=category_bmi(BMI)

        print(f"\nYour BMI is: {BMI:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
