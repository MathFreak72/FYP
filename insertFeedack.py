from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import OperationTimedOut
import uuid

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# global_session = None

def driver_feedback(session):
    @app.post("/driver")
    async def user(safety_rating: int, cleanliness_rating: int, punctuality: int, cancelled_ride: int, overall_rating: int):
        try:
            insert_query = """INSERT INTO driverdb.drivers(driver_id, created_at, safety_rating, cleanliness_rating, punctuality, cancelled_ride, overall_rating) 
                              VALUES(uuid(), toTimeStamp(now()), %s, %s, %s, %s, %s)"""
            session.execute(insert_query,
                                   (safety_rating, cleanliness_rating, punctuality, cancelled_ride, overall_rating))
            return {"Message": "Driver's feedback successfully entered."}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

def user_feedback(session):
    @app.post("/user")
    async def user(trust_rating: int, cleanliness_rating: int, punctuality: int, cancelled_ride: int, overall_rating: int):
        try:
            insert_query = """INSERT INTO driverdb.users(driver_id, created_at, trust_rating, cleanliness_rating, punctuality, cancelled_ride, overall_rating) 
                              VALUES(uuid(), toTimeStamp(now()), %s, %s, %s, %s, %s)"""
            session.execute(insert_query,
                                   (trust_rating, cleanliness_rating, punctuality, cancelled_ride, overall_rating))
            return {"Message": "User's feedback successfully entered."}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
