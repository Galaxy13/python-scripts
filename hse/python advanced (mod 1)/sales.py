import sys

customer_dict = {}
for input_line in sys.stdin:
    if input_line == '\n':
        break
    name, product, quantity = input_line.rstrip('\n').split()
    if not customer_dict.get(name):
        customer_dict[name] = {product: 0}
    if not customer_dict[name].get(product):
        customer_dict[name][product] = 0
    customer_dict[name][product] += int(quantity)
for name in sorted(customer_dict):
    print(name + ':')
    for product in sorted(customer_dict[name]):
        print(product, customer_dict[name][product])

# a063d36b87a583a17cc3861f758fb1af