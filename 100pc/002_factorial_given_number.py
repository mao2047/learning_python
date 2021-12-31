def factorial (number):
    product = 1
    for element in range(1, number+1):
        product = product * element
    print(product)

number = int(input("intrudizca numero: "))
factorial(number)
