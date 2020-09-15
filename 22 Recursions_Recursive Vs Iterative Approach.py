"""
Understanding the iterative vs recursive approach using factorial example
n!=n(n-1)(n-2)(n-3)(n-4).......1
n!=n*(n-1)!
"""

def factorial_iterative(number):
    """
               :param number: Integer
               :return: number * number-1 * number-2 * number-3.......1
    """
    fac=1
    for i in range(number):
        fac=fac*(i+1)
    return fac

def factorial_recursive(number):
    """
            :param number: Integer
            :return: number * number-1 * number-2 * number-3.......1
    """
    if number==1:
        return 1
    else:
        return (number * factorial_recursive(number-1))
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120


number1=int(input("Enter the number to calculate it's factorial: "))
print("Factorial using iterative: ",factorial_iterative(number1))
print("Factorial using recursive: ",factorial_recursive(number1))
