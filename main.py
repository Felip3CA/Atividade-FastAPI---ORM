from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db
from models import Categoria, Produto

app = FastAPI(title="Vendo comida")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
     request,
    "comida.html",
    {"request": request}
    )

@app.get("/produto/cadastro", response_class=HTMLResponse)
def exibir_cadastro(request: Request):
    return templates.TemplateResponse(request, "cadastro_produto.html", {"request": request})
