from pant import Pants
from saleperson import SalesPerson

pant1 = Pants('red', 35, 36, 15.33)
pant2 = Pants('blue', 32, 38, 24.12)
pant3 = Pants('black', 28, 30, 8.14)

salesperson = SalesPerson('AA', 'BB', 123, 40000)
salesperson.sell_pants(pant1)
salesperson.sell_pants(pant2)
salesperson.sell_pants(pant3)

salesperson.display_sales()
print(salesperson.calculate_sales())
print(salesperson.calculate_commission(0.1))