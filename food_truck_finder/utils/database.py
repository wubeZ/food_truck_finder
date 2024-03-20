import os
import mongoengine
from dotenv import load_dotenv

load_dotenv()

# Global database connection instance
db_connection = None

def connect_to_mongodb_atlas(mongo_url):
    global db_connection
    if db_connection is None:
        try:
            # Connect to MongoDB Atlas
            db_connection = mongoengine.connect(host=mongo_url,alias='default')
            print("Connected to MongoDB Atlas successfully.")
        except Exception as e:
            print(f"Error connecting to MongoDB Atlas: {e}")

    return db_connection

def get_database():
    
    mongo_url = os.getenv("MONGO_URL")
    
    # Connect to MongoDB Atlas and return the database connection instance
    return connect_to_mongodb_atlas(mongo_url)
