import value_operations
from fizzbuzz import fizzbuzz


print(__name__)

if __name__ == "__main__":
    results = value_operations.swap(5, 1)
    print(results)


    # from value_operations import swap


    # results = swap(5, 1)
    # print(results)


    number = 3
    print(number)

    name = "Kan"
    print(name)

    if number == 3:
        print("Number is 3")
        print("Inside IF")

    print("Outside IF")

    fruits = ["Orange", "Apple", "Durian"]  # iterable
    print(fruits[0])

    # Bad
    for i in range(0, len(fruits)):
        print(i, fruits[i])

    # Good
    for fruit in fruits:
        print(fruit)

    # Good
    for i, fruit in enumerate(fruits):
        print(i, fruit)

    company = ("GitHub", "SF, USA")
    company_name, location = company
    print(company_name, location)

    a = 5
    b = 10
    a, b = b, a  # (10, 5)

    # tmp = a
    # a = b
    # b = tmp

    print(a, b)

    print(value_operations.swap(1, 2))

    for number in range(0, 16):
        print(number, fizzbuzz(number))