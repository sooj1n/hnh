from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi import Request
import random
from transformers import pipeline
import io
from hnh.utils import get_max_label

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
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog") 
    return {"Hello": random.choice(["hotdog", "not hotdog"])}



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # 파일 저장
    img = await file.read()
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    
    from PIL import Image
    img = Image.open(io.BytesIO(img))  # 이미지 바이트를 PIL 이미지로 변환
    
    p = model(img)
    label = get_max_label(p)
    #{'label': 'hot dog', 'score': 0.54},
    #{'label': 'not hot dog', 'score': 0.46}

    return {"label": label, "p": p} 
