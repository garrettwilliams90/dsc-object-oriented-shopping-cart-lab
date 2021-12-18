class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        
    def add_item(self, name, price, quantity=1):
        for i in range(quantity):
            self.items.append({"name":name,"price":price})
            self.total = self.total + price
        return self.total
    
    def mean_item_price(self):
        mean_ = (self.total)/(len(self.items))
        return mean_

    def median_item_price(self):
        from operator import itemgetter
        newlist_ = sorted(self.items, key = itemgetter('price'))
        if len(newlist_)%2 == 1:
            return newlist_[np.rint(len(newlist_)/2).astype(int)]['price']
        else:
            first_ = newlist_[int(len(newlist_)/2)]['price']
            second_ = newlist_[int((len(newlist_)/2)-1)]['price']
            return (first_ + second_)/2

    def apply_discount(self):
        if self.employee_discount == 0 or self.employee_discount is None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            return self.total - (self.total*(self.employee_discount/100))

    def void_last_item(self):
        if len(self.items) == 0:
            return "There are no items in your cart!"
        else:
            self.total = self.total - self.items[-1]['price']
            self.items.pop()
            return self.total
        #SOLUTION
#         if self.items:
#             removed_item = self.items.pop()
#         else:
#             return "There are no items in your cart!"
#         self.total -= removed_item['price']
            