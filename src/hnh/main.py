from typing import Union
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request

import random

app = FastAPI()

html = Jinja2Templates(directory="public")

@app.get("/hello")
def read_root():
    return {"Hello": "hotdog"}

@app.get("/")
async def home(request: Request):
    hotdog = "https://www.dailiang.co.kr/news/photo/201111/34714_19009_5246.jpg"
    coolcat = "https://image.fmkorea.com/files/attach/new3/20230527/486616/5032171247/5810153990/e5bc995f67dc592ba0121714373baf8c.jpeg"
    image_url = random.choice([hotdog, coolcat])
    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})


@app.get("/predict")
def hotdog():
    
    return {"Hello": random.choice(["hotdog", "not hotdog"])}
