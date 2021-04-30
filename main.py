from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import date


app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/hello", response_class = HTMLResponse)
def root(request: Request):
    today = date.today().strftime("%Y-%m-%d")
    return templates.TemplateResponse('index.html', {'request': request, 'today': today})
