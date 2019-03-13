class Apparel:
    counter=100
    def __init__(self,price,item_type):
        self.price=price
        self.item_type=item_type
        self.item_id=None
        Apparel.counter+=1
        if item_type=='Cotton':
            self.item_id='C'+str(Apparel.counter)
        if item_type=='Silk':
            self.item_id='S'+str(Apparel.counter)
    def calculate_price(self):
        p=self.get_price()*1.05
        self.set_price(p)
    def get_item_id(self):
        return self.item_id
    def get_price(self):
        return self.price
    def get_item_type(self):
        return self.item_type
    def set_price(self,price):
        self.price=price

class Cotton(Apparel):
    def __init__(self,price,discount):
        super().__init__(price,'Cotton')
        self.discount=discount
    def calculate_price(self):
        super().calculate_price()
        p=super().get_price()*((100-self.get_discount())/100)
        p*=1.05
        super().set_price(p)
    def get_discount(self):
        return self.discount
class Silk(Apparel):
    def __init__(self,price):
        super().__init__(price,'Silk')
        self.points=None
    def calculate_price(self):
        super().calculate_price()
        p=super().get_price()
        if p>10000:
            self.points=10
        else:
            self.points=3
        p*=1.10
        super().set_price(p)
    def get_points(self):
        return self.points
    
ob1=Cotton(100,10)
ob2=Silk(100)
ob1.calculate_price()
ob2.calculate_price()
print('Cotton Object details:\n')
print(ob1.get_item_id(),ob1.get_item_type(),ob1.get_price(),ob1.get_discount())
print('Silk Object details:\n')
print(ob2.get_item_id(),ob2.get_item_type(),ob2.get_price(),ob2.get_points())