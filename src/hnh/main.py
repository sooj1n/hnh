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
    #img = "file:///C:/Users/Playdata2/Downloads/686fdbf4-cdd1-4d63-ab74-fe5224519d3a%20(1).webp"
    image_url = random.choice([hotdog])
    return html.TemplateResponse("index.html",{"request":request, "image_url": image_url})


@app.get("/predict")
def hotdog():
    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog") 
    return {"Hello": random.choice(["hotdog", "not hotdog"])}



@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    file_location = f"static/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    model = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")
    img = Image.open(file_location)
    p = model(img)
    label = get_max_label(p)

    # 파일 경로와 분류 결과 반환
    return {"label": label, "p": p, "url": f"/static/{file.filename}"}
