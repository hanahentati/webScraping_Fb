# Fb_scrapping

This project is a facebook scrapping app for posts using fastapi and that save the scrapping data in database in this case is mongodb

### to start the app 
git clone https://github.com/hanahentati/Fb_scrapping


so to start this locally you have to create a local database and change the mongodb url in the config.py
make sure to run 

- pip install -r requirements.txt 
to install all dependencies

To start the app locally:
- uvicorn main:app --reload

in the **utils.py** if you have the chromedriver install in your device just change the path in the function 
**initialize_driver():** and add your **login and password** in the funvtion 
