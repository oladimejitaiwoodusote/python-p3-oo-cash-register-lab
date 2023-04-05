#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.log = []
    
  
  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    #self.items.append(item)
    for i in range(quantity):
      self.items.append(item)

    self.log.append(price * quantity)

  def apply_discount(self):
    if (self.discount == 0):
      print("There is no discount to apply.")
    
    else: 
      self.total = int(self.total * (1 - (self.discount/100)))
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    self.total = self.total - self.log[len(self.log)-1]
    pass
    


brock = CashRegister()
brock.add_item("tomato", 1.76, 2)
brock.apply_discount()
print(brock.items)
print(brock.log)
brock.void_last_transaction()
print(brock.items)
print(brock.log)
