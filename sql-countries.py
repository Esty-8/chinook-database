from sqlalchemy import (
    create_engine, Column, Integer, Float, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Countries" table
class Countries(base):
    __tablename__ = "Countries"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital_name = Column(String)
    population_name = Column(Float)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above 
session = Session()

#creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Countries table
spain_country = Countries(
    country_name = "Spain",
    capital_name = "Madrid",
    population_name = 3.793

) 

portugal_country = Countries(
    country_name = "Portugal",
    capital_name = "Praga",
    population_name = 3.763

)

germany_country = Countries(
    country_name = "Germany",
    capital_name = "Berlin",
    population_name = 3.356

)

ireland_country = Countries(
    country_name = "Ireland",
    capital_name = "Dublin",
    population_name = 3.973

)

# updating a single word
# country = session.query(Countries).filter_by(id=2).first()
# country.population_name = 222.2

# add each instance of our countries to our session
session.add(spain_country)
# session.add(portugal_country)
# session.add(germany_country)
# session.add(ireland_country)


# commit our session to the database
session.commit()

# deleting a single word
# country = session.query(Countries).filter_by(id=1).first()
# session.delete(country)
# session.commit()



# query the database to find all Countries
countries = session.query(Countries)
for country in countries:
    print(
        country.id,
        country.country_name,
        country.capital_name,
        country.population_name,
        sep=" | "

    )




