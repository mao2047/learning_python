def my_dict(number):
    powers = {}
    for element in range(1, number+1):
        powers[element] = element*element
    print(powers)


number = int(input("introduzca numero: "))
my_dict(number)
