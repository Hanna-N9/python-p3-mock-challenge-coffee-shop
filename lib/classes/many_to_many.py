# from statistics import mean

class Coffee:
    def __init__(self, name):
        self.name = name
            
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
     
    #Object Relationship Methods and Properties   
    #Returns a list of all orders for that coffee
    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    #Object Relationship Methods and Properties 
    #Returns a unique list of all coffees a customer has ordered, Coffees must be of type Coffee
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    #Aggregate and Association Methods
    #Returns the total number of times a coffee has been ordered, Returns 0 if the coffee has never been ordered   
    def num_orders(self):
        return len(self.orders())
    
    #Aggregate and Association Methods
    #Returns the average price for a coffee based on its orders, Returns 0 if the coffee has never been ordered, Reminder: you can calculate the average by adding up all the orders prices and dividing by the number of orders
    def average_price(self):
        prices = [order.price for order in self.orders() if order.coffee == self] 
        return sum(prices) / len(prices)
    
        #Another option
        # return mean([order.price for order in self.orders()])



class Customer:
    all = []
    
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
            
    #Object Relationship Methods and Properties   
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    #Object Relationship Methods and Properties 
    def coffees(self):
       return list({order.coffee for order in self.orders()})

    #Aggregate and Association Methods
    #Receives a coffee object and a price number as arguments, Creates and returns a new Order instance and associates it with that customer and the coffee object provided.
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
   
   
   
   
   
class Order:
    all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float) and 1.0 <= price <= 10.0 and not hasattr(self, "price"):
            self._price = price
            
    #Object Relationship Methods and Properties
    #Returns the customer object for that order, Must be of type Customer
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
            
    #Object Relationship Methods and Properties
    #Returns the coffee object for that order, Must be of type Coffee
    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee