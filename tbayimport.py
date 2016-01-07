from tbay import User, Item, bid, session

Charlie = User(user_name="Cgozalez", password="freya")
session.add(Charlie)

Daniel = User(user_name="Dsmith", password="blue")
session.add(Daniel)

Spec = Item(name="Spec", description="design")
session.add(Spec)

Blackrain = Item(name="Black Rain",description="cloud")
session.add(Blackrain)
session.commit()

print (session.query(User).all())