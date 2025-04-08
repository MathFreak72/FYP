import uuid
import random

def insert_driver_ratings(session):
    insert_query = session.prepare("""
        INSERT INTO driverdb.drivers (driver_id, created_at, safety_rating, cleanliness_rating, punctuality, cancelled_ride, overall_rating)
        VALUES (?, toTimeStamp(now()), ?, ?, ?, ?, ?)
    """)

    unique_drivers = [uuid.uuid4() for _ in range(100)]  # Generate 100 unique driver IDs

    for driver_id in unique_drivers:
        for _ in range(5):  # Insert 5 ratings per driver
            # created_at = datetime.utcnow()
            safety_rating = random.randint(1, 5)
            cleanliness_rating = random.randint(1, 5)
            punctuality = random.randint(1, 5)
            cancelled_ride = random.randint(1, 5)
            overall_rating = random.randint(1, 5)

            session.execute(insert_query, (driver_id, safety_rating, cleanliness_rating, punctuality, cancelled_ride, overall_rating))

def insert_user_ratings(session):
    insert_query = session.prepare("""
        INSERT INTO driverdb.users (user_id, created_at, trust_rating, cleanliness_rating, punctuality, cancelled_ride, overall_rating)
        VALUES (?, toTimeStamp(now()), ?, ?, ?, ?, ?)
    """)

    unique_users = [uuid.uuid4() for _ in range(100)]  # Generate 100 unique user IDs

    for user_id in unique_users:
        for _ in range(5):  # Insert 5 ratings per driver
            # created_at = datetime.utcnow()
            trust_rating = random.randint(1, 5)
            cleanliness_rating = random.randint(1, 5)
            punctuality = random.randint(1, 5)
            cancelled_ride = random.randint(1, 5)
            overall_rating = random.randint(1, 5)

            session.execute(insert_query, (user_id, trust_rating, cleanliness_rating, punctuality, cancelled_ride, overall_rating))

