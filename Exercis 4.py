first_number = int(input("first number: "))
second_number = int(input("second number: "))
third_number = int(input("third number: "))
fourth_number = int(input("fourth number: "))
largest_number = max(first_number,second_number,third_number,fourth_number)

if fourth_number > first_number and fourth_number > second_number and fourth_number > third_number:
    largest_number = fourth_number
elif second_number > first_number and second_number > third_number:
    largest_number = second_number
elif first_number > third_number:
    largest_number = first_number
else:
    largest_number = third_number
 
print(f'the largest number is {largest_number}')