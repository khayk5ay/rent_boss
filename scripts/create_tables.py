from tables import engine, session, ListingReviews
from my_sql_engine import Engine, Base
from sqlalchemy import Column, Integer, String, DateTime


for table in Base.metadata.tables:
    print(table)

if __name__ == "__main__":
    Base.metadata.create_all(engine)

session.bulk_save_objects()
session.commit()


"""
Make an empty list
For each row in the csv, create an object with the specifics and append to the list

Example: ppr_raw_objects.append(
                PprRawAll(
                    date_of_sale=update_date_of_sale(row["date_of_sale"]),
                    address=transform_case(row["address"]),
                    postal_code=transform_case(row["postal_code"]),
                    county=transform_case(row["county"]),
                    price=update_price(row["price"]),
                    description=update_description(row["description"]),
                )
            )

session.bulk_save_objects(ppr_raw_objects)
session.commit
"""


