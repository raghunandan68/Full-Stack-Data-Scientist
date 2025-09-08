class Order:
    def __init__(self,items):
        self.items={}
    def add(self,item,price):
        self.items[item]=price
    def remove(self,item):
        if item in self.items:
            del self.items[item]
    def calculate_total(self):
        count=0
        for k,v in self.items.items():
            count+=v
        return count
    def show_items(self):
        for k,v in self.items.items():
            print(k," : ",v)
o = Order({})
o.add("Shirt", 500)
o.add("Shoes", 1500)
print(o.calculate_total())
o.show_items()