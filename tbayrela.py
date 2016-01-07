from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    passport = relationship("Passport", uselist=False, backref="owner")

class Passport(Base):
    __tablename__ = 'passport'
    id = Column(Integer, primary_key=True)
    issue_date = Column(Date, nullable=False, default=datetime.utcnow)

    owner_id = Column(Integer, ForeignKey('person.id'), nullable=False)

beyonce = Person(name="Beyonce Knowles")
passport = Passport()
beyonce.passport = passport

session.add(beyonce)
session.commit()

print(beyonce.passport.issue_date)
print(passport.owner.name)

#uselist=False 
#The uselist=False argument says that the passport should 
#be treated as a single object rather than a list of objects. 
#This is what guarantees that this is a one-to-one relationship - 
#each person only has one set of passport information.

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Manufacturer(Base):
    __tablename__ = 'Manufacturer'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    guitars = relationship("Guitar", backref="manufacturer")  
    #foreign key relationship
    
class Guitar(Base):
    __tablename__ = 'Guitar'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'),
                             nullable=False)

fender = Manufacturer(name="Fender")
strat = Guitar(name="Stratocaster", manufacturer=fender)
tele = Guitar(name="Telecaster")
fender.guitars.append(tele)

session.add_all([fender, strat, tele])
session.commit()

for guitar in fender.guitars:
    print(guitar.name)
print(tele.manufacturer.name)

#look at the appended (tele)
#why one is capitalized and not the (m) on Gruitar , Manu.......

#A one-to-many relationship is constructed in the same way as a one-to-one 
#relationship except that the uselist=False argument is omitted. For example, 
#here's a one-to-many relationship between manufacturer and the guitars they produce:

from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

pizza_topping_table = Table('pizza_topping_association', Base.metadata,
    Column('pizza_id', Integer, ForeignKey('pizza.id')),
    Column('topping_id', Integer, ForeignKey('topping.id'))
                           )

class Pizza(Base):
    __tablename__ = 'pizza'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    toppings = relationship("Topping", secondary="pizza_topping_association",
                            backref="pizzas")

class Topping(Base):
    __tablename__ = 'topping'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

peppers = Topping(name="Peppers")
garlic = Topping(name="Garlic")
chilli = Topping(name="Chilli")

spicy_pepper = Pizza(name="Spicy Pepper")
spicy_pepper.toppings = [peppers, chilli]

vampire_weekend = Pizza(name="Vampire Weekend")
vampire_weekend.toppings = [garlic, chilli]


session.add_all([garlic, peppers, chilli, spicy_pepper, vampire_weekend])
session.commit()

for topping in vampire_weekend.toppings:
    print(topping.name)

for pizza in chilli.pizzas:
    print(pizza.name)


#The table will hold foreign keys to columns on both sides of the relationship. 
#For example, here's a many-to-many relationship between pizzas and toppings: