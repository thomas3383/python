import string
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase

numbers = input("Enter a list of numbers separated by a comma...\n").split(", ")
while(
    (str(numbers) in lower_case)
    or
    (str(numbers) in upper_case)
    ):
    print("Invalid numbers; it is not a number\n")
    numbers = input("Enter a list of numbers separated by a comma...\n").split(", ")
    continue


if(
    (str(numbers) not in lower_case)
    or
    (str(numbers) not in upper_case)
    ):
    biggest_number = 0.0
    
    for i in range(len(numbers)):
        number = numbers[i]
        if float(number) > biggest_number:
            biggest_number = float(number)
    print(f"The biggest number is {biggest_number}\n")
