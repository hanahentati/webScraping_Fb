# Fb_scrapping

This project is a facebook scrapping app for public pages using fastapi and that save the scrapping data in database in this case is mongodb

### to start the app 
git clone https://github.com/hanahentati/Fb_scrapping

In case of using docker to start the application:

docker-compose up -d
this command will start Fastapi and mongodb
For starting the scraper, open up your browser and enter:
http://127.0.0.1/

In case of not using docker clone the git  
so to start this locally you have to create a local database and change the mongodb url in the config.py
make sure to run 

pip install -r requirements.txt 
to install all dependencies

To start the app locally:
uvicorn main:app --reload

in the utils.py if you have the chromedriver install in your device just change the path in the function 
initialize_driver():
else you can download the chromedriver automatically using the code just uncomment the code in comment 
it will also Check if the current version of chromedriver exists
