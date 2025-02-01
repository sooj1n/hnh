# hnh 🌭

# 핫도그 이미지 판별기 💻🤖

## 프로젝트 개요

이 프로젝트는 FastAPI를 사용하여 업로드된 이미지가 핫도그인지 아닌지를 판별하는 웹 애플리케이션입니다. 사용자는 이미지를 업로드하면 모델이 해당 이미지를 분석하여 결과를 반환합니다.

## 주요 기능

- **이미지 업로드**: 사용자가 로컬에서 이미지를 업로드할 수 있습니다.
- **이미지 판별**: 업로드된 이미지가 핫도그인지 아닌지를 판별합니다.
- **결과 표시**: 판별 결과에 따라 해당 이미지를 표시합니다.

## 설치 및 실행 방법

### 필수 조건

- Python 3.x

### 패키지 설치

아래 명령어를 사용하여 필요한 패키지를 설치합니다:

```bash
pip install fastapi uvicorn jinja2
```

### 프로젝트 구조

프로젝트의 디렉토리 구조는 다음과 같습니다:

```
프로젝트/
├── main.py
├── public/
│   └── index.html
└── README.md
```

### 애플리케이션 실행

아래 명령어를 사용하여 FastAPI 애플리케이션을 실행합니다:

```bash
uvicorn main:app --reload
```

서버가 실행되면 브라우저에서 `http://localhost:8000`으로 접속하여 애플리케이션을 사용할 수 있습니다.

## 주요 코드 설명

### `main.py`

FastAPI를 사용하여 웹 서버를 설정하고, Jinja2를 통해 템플릿을 렌더링합니다. `/` 경로로 접속하면 랜덤으로 핫도그 또는 고양이 이미지가 표시됩니다.

```python
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()
templates = Jinja2Templates(directory="public")

@app.get("/")
async def home(request: Request):
    hotdog = "https://www.dailiang.co.kr/news/photo/201111/34714_19009_5246.jpg"
    coolcat = "https://image.fmkorea.com/files/attach/new3/20230527/486616/5032171247/5810153990/e5bc995f67dc592ba0121714373baf8c.jpeg"
    image_url = random.choice([hotdog, coolcat])
    return templates.TemplateResponse("index.html", {"request": request, "image_url": image_url})
```

### `index.html`

Jinja2 템플릿을 사용하여 이미지를 동적으로 표시합니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Classification</title>
</head>
<body>
    <h1>GIVE ME HOTDOG</h1>
    {% if image_url %}
    <h2>Here is your image:</h2>
    <img src="{{ image_url }}" width="300">
    {% endif %}
</body>
</html>
```

### if hotdog
![image](https://github.com/user-attachments/assets/236080fc-0fe1-4e05-8a85-56f577e5231c)

### if not hotdog
![image](https://github.com/user-attachments/assets/b275489a-3b2b-4e8f-8d57-3fbc408c8316)


## 참고 자료
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Jinja2 공식 문서](https://jinja.palletsprojects.com/)

## 블로그 링크
- https://soojin1.tistory.com/23

  
