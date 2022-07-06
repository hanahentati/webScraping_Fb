import motor.motor_asyncio
import os
"""
to work on local without docker you can uncomment these two lines of code 

# Mongodb_URL = 'mongodb://localhost:27017'

# client = motor.motor_asyncio.AsyncIOMotorClient(Mongodb_URL)

"""
Mongodb_URL = 'mongodb://localhost:27017'

client = motor.motor_asyncio.AsyncIOMotorClient(Mongodb_URL)
"""
 we are using os.environ["DB_URL"] to get the mongodb Connection String URI Format which is passed in the docker-compose 
 """
# client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["DB_URL"])
# connect to database

database = client.TestScDB