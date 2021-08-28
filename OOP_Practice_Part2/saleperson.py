class SalesPerson:
    def __init__(self,first_name,last_name,employee_id,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_obj):
        self.pants_sold.append(pants_obj)

    def display_sales(self):
        for pant in self.pants_sold:
            print('color: {}, waist size: {}, lenght: {}, price:{}'.
            format(pant.color,pant.waist_size, pant.length, pant.price))

    def calculate_sales(self):
        total = 0
        for pant in self.pants_sold:
            total += pant.price

        self.total_sales = total
        return total

    def calculate_commission(self, percentage):
        total_sale = self.calculate_sales()
        return percentage * total_sale