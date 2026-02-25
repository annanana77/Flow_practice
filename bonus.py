#get salary, has to be positive, more than 0, numeric (can be float)
while True:
    try:
        sal=float(input("Input your monthly salary: "))
        if sal <= 0:
            print("Salary must be a positive number.")
        else:
            break
    except ValueError:
        print("Please enter a valid number for salary.")
#get years, has to be positive, can be 0 (if worked less than a year), numeric (int because full years only)
while True:
    try:
        yrs=int(input("Input your years of service: "))
        if yrs < 0:
            print("Years of service cannot be negative.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer for years of service.")
# if service over 2 years, for every year 15% bonus
if yrs > 2:
    yrs_overtwo = yrs - 2
    bonus = (sal * 0.15) * yrs_overtwo
    print(f"Your bonus is: {bonus:.2f}")
else:    
    print("Unfortunately, you are not eligible for a bonus yet.")