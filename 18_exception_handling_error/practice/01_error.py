try:
    num = int(input("Enter the number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Hey, you cannot divide by zero this is not acceptable.")
except ValueError:
    print("Invalid input! Please enter an number")


# Another way to do this.

try:
    num = int(input("Enter the number: "))
    result = 10 / num
    print(result)
except (ValueError, ZeroDivisionError) as e:
    print(f"An error occured {e}")