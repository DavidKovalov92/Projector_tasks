first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
choose_operation = input("Choose operation: ")

if choose_operation == "+":
    print(first_num + second_num)
elif choose_operation == "-":
    print(first_num - second_num)
elif choose_operation == "*":
    print(first_num * second_num)