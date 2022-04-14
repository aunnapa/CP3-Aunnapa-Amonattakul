class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Add product to", self.name, self.lastname, "'s cart")

customer1 = Customer()
customer1.name = "Aunnapa"
customer1.lastname = "A"
customer1.addCart()

customer2 = Customer()
customer2.name = "BBBBBB"
customer2.lastname = "B"
customer2.addCart()

customer3 = Customer()
customer3.name = "CCCCCC"
customer3.lastname = "C"
customer3.addCart()

customer4 = Customer()
customer4.name = "DDDDDD"
customer4.lastname = "D"
customer4.addCart()