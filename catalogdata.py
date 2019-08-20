from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, CategoryItem, Base, User

engine = create_engine('sqlite:///catalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user

User1 = User(name="Sample User", email="abc@sample.com",
             picture="""https://pbs.twimg.com/profile_images/2671170543/
             18debd694829ed78203a5a36dd364160_400x400.png""")
session.add(User1)
session.commit()


cat1 = Category(name='Soccer')
session.add(cat1)
session.commit()

cat2 = Category(name='Basketball')
session.add(cat2)
session.commit()

cat3 = Category(name='Baseball')
session.add(cat3)
session.commit()

cat4 = Category(name='Frisbee')
session.add(cat4)
session.commit()

cat5 = Category(name='Rock Climbing')
session.add(cat5)
session.commit()

cat6 = Category(name='Foosball')
session.add(cat6)
session.commit()

cat7 = Category(name='Skating')
session.add(cat7)
session.commit()

cat8 = Category(name='Hockey')
session.add(cat8)
session.commit()

cat9 = Category(name='Snowboarding')
session.add(cat9)
session.commit()

item1 = CategoryItem(user_id=1, name='Hockey stick',
                     description="""A hockey stick is a piece of
                     sport equipment used by the players in all the forms
                     of hockey to move the ball or puck (as appropriate to
                     the type of hockey) either to push, pull,hit, strike,
                     flick, steer, launch or stop the ball""",
                     category=cat8)
session.add(item1)
session.commit()

item2 = CategoryItem(user_id=1, name='Quickdraws',
                     description="""Quickdraws (often referred to as "draws")
                     are used by climbers to connect ropes to bolt anchors,
                     or to other traditional protection, allowing the rope
                     to move through the anchoring system with
                     minimal friction""",
                     category=cat5)
session.add(item2)
session.commit()

item3 = CategoryItem(user_id=1, name='Frisbee',
                     description="""A frisbee is also called a flying disc
                     or simply a disc and is a gliding toy or sporting item
                     that is generally plastic and roughly 8 to 10 inches
                     in diameter with a pronounced lip. It is used
                     recreationally and competitively for throwing and
                     catching, as in flying disc games.""",
                     category=cat4)
session.add(item3)
session.commit()

item4 = CategoryItem(user_id=1, name='Snowboard',
                     description="""Snowboards are boards where both feet
                     are secured to the same board, which are wider than
                     skis,with the ability to glide on snow.Snowboards widths
                     are between 6 and 12 inches or 15 to 30 centimeters.
                     Snowboards are differentiated from monoskis by
                     the stance of the user.""",
                     category=cat9)
session.add(item4)
session.commit()

print("added menu items!")
