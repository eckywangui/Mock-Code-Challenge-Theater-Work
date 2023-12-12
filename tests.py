
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models import Base, Role, Audition


engine = create_engine('sqlite:///theater.db')

# Create a session class
Session = sessionmaker(bind=engine)

# Create an instance of the session
session = Session()

# Create tables
Base.metadata.create_all(engine)


role1 = Role(character_name='Role 1')
audition1 = Audition(actor='Actor 1', location='Location 1', role=role1)
audition2 = Audition(actor='Actor 2', location='Location 2', role=role1)

# Add data to the session and commit to the database
session.add_all([role1, audition1, audition2])
session.commit()


role = session.query(Role).filter_by(character_name='Role 1').first()

print("Actors:", role.actors())
print("Locations:", role.locations())
print("Lead:", role.lead())
print("Understudy:", role.understudy())

# Close the session
session.close()
