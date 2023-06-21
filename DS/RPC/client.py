import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")
print("Connected to localhost 6789")
while True:
    print("1>Add two numbers",
          "2>Subtract two numbers",
          "3>Multiply two numbers",
          "4>Divide two numbers",
          "5>Exit",
          sep="\n")
    choice = int(input('Enter choice: '))
    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter two number: "))
        result = proxy.add(num1,num2)
        print(f"Addition is {result}")
    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter two number: "))
        result = proxy.subtract(num1,num2)
        print(f"Subtraction is {result}")
    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter two number: "))
        result = proxy.multiply(num1,num2)
        print(f"Multiplication is {result}")
    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter two number: "))
        result = proxy.divide(num1,num2)
        print(f"Quotient is {result[0]}\nRemainder is {result[1]}")
    elif choice == 5:
        break
        
'''OUTPUT
python3 client.py 
Connected to localhost 6789
1>Add two numbers
2>Subtract two numbers
3>Multiply two numbers
4>Divide two numbers
5>Exit
Enter choice: 1
Enter first number: 15
Enter two number: 75
Addition is 90
1>Add two numbers
2>Subtract two numbers
3>Multiply two numbers
4>Divide two numbers
5>Exit
Enter choice: 2
Enter first number: 87
Enter two number: 45
Subtraction is 42
1>Add two numbers
2>Subtract two numbers
3>Multiply two numbers
4>Divide two numbers
5>Exit
Enter choice: 3
Enter first number: 56
Enter two number: 14
Multiplication is 784
1>Add two numbers
2>Subtract two numbers
3>Multiply two numbers
4>Divide two numbers
5>Exit
Enter choice: 4
Enter first number: 91
Enter two number: 13
Quotient is 7
Remainder is 0
'''
