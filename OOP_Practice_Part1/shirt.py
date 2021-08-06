class Shirt:
    def __init__(self,shirt_color,shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)

### TODO:
# - insantiate a shirt object with the following characteristics:
# - color red, size S, style long-sleeve, and price 25
# - store the object in a variable called shirt_one
#
###


### TODO:
# - print the price of the shirt using the price attribute
# - use the change_price method to change the price of the shirt to 10
# - print the price of the shirt using the price attribute
# - use the discount method to print the price of the shirt with a 12% discount
#
###

### TODO:
#
# - instantiate another object with the following characteristics:
# - color orange, size L, style short-sleeve, and price 10
# - store the object in a variable called shirt_two
#
###

### TODO:
#
# - use the shirt discount method to calculate the total cost if
#       shirt_one has a discount of 14% and shirt_two has a discount
#       of 6%
# - store the results in a variable called total_discount
###
