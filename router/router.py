from config import database
from scraper.scrape import FacebookScrapping
from scraper.utils import *
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates/")


@router.get("/")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request, 'result': ""})

@router.post("/")
async def form_post(request: Request, name: str = Form(...), timeout: int = 100):
    result = check_page_exists(name)
    if not result:
        return templates.TemplateResponse('form.html', context={'request': request, 'result': "this page doesn't exist "
                                                                                              "named {}".format(name),'title': name})
    else:
        fb_scrapping = FacebookScrapping(name, timeout)
        fb_scrapping.init_driver()

        data = fb_scrapping.scrape_data()

        for i in range(len(data)):
             await database[name].insert_one(data[i])

        post_in_page = await database[name].find().to_list(1000)
        docs = []
        for doc in post_in_page:
            doc.pop('_id')
            docs.append(doc)
        return templates.TemplateResponse('table.html', context={'request': request, 'title': name, 'posts': docs})

