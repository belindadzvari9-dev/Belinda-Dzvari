#4. Product of Multiples
def product_of_multiples(factor, limit):
    product = 1

    # Start at factor and stop before limit.
    for number in range(factor, limit, factor):
        product = product * number

    return product


print(product_of_multiples(3, 10))
Output:
162
#Explanation: the multiples of 3 below 10 are 3, 6, and 9. Therefore:
3 × 6 × 9 = 162
