from config import database
from scraper.scrape import FacebookScrapping
from scraper.utils import *
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
import csv
import json
import numpy as np

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('first_page.html', context={'request': request, 'result': ""})

@router.post("/")
async def form_post(request: Request, name: str = Form(...)):
    result = check_page_exists(name)
    if not result:
        return templates.TemplateResponse('first_page.html', context={'request': request, 'result': "this page doesn't exist "
                                                                                              "named {}".format(name),'title': name})
    else:
        fb_scrapping = FacebookScrapping(name)
        fb_scrapping.init_driver()

        data = fb_scrapping.scrape_data()

        for i in range(len(data)):
             await database[name].insert_one(data[i])

        post_in_page = await database[name].find().to_list(1000)
        docs = []
        for doc in post_in_page:
            doc.pop('_id')
            docs.append(doc)
            #save the data into a json file
            json_object = json.dumps(docs)
            with open("scrapped_data.json", "w") as outfile:
                outfile.write(json_object)
            print(json_object)
            #for more clarity it's displayed in a table
        return templates.TemplateResponse('scrapped_data.html', context={'request': request, 'title': name, 'posts': docs})

