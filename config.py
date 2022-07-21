import motor.motor_asyncio
import os
"""
to work on local without docker you can uncomment these two lines of code 

"""
Mongodb_URL = 'mongodb://localhost:27017'

client = motor.motor_asyncio.AsyncIOMotorClient(Mongodb_URL)

# connect to database

database = client.testFbsc