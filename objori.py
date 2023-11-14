#https://www.youtube.com/watch?v=MikphENIrOo
class Customer:
    def __init__(self, name,membership_type) :
       self.name = name
       self.membership_type = membership_type
       print("customer created")
c = Customer("galeb", "gold")
print(c.name, c.membership_type)

c2 = Customer("brad", "bronze")
print(c2.name,c2.membership_type)

c3 = Customer("rita", "silver")
print(c3.name, c3.membership_type)

Customers = [Customer("galeb", "gold"),Customer("brad", "bronze") ]

print(Customers[0].name)
print(Customers[1].name)
        