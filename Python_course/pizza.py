def make_pizza(size, *toppings):
    print(f"\n Making a {size}-inch pizza with the folllowing toppings :")
    for topping in toppings:
        print(f"-{topping}")

    