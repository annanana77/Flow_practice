while True:
    try:
        sal=float(input("Input your monthly salary: "))
        if sal <= 0:
            print("Salary must be a positive number.")
        else:
            break
    except ValueError:
        print("Please enter a valid number for salary.")

while True:
    try:
        yrs=int(input("Input your years of service: "))
        break 
    except ValueError:
        print("Please enter a valid integer for years of service.")

if yrs > 2:
    bonus = (sal * 0.15) * (yrs-2)
    print(f"Your bonus is: {bonus:.2f}")
else:    
    print("Unfortunately, you are not eligible for a bonus yet.")