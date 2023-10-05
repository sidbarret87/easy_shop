from fastapi import FastAPI, Depends, Form
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates



from models import *
from database import get_db

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Эндпойнты для товаров
@app.post("/products/", response_model=ProductCreate)
def create_product(request: Request,
                   name: str = Form(...),
                   description: str = Form(...),
                   price: float = Form(...),
                   db: Session = Depends(get_db) ):
    product_data = ProductCreate(name=name, description=description, price=price)
    product = Product(**product_data.dict())
    db.add(product)
    db.commit()
    db.refresh(product)
    return templates.TemplateResponse("index.html", {"request": request, "created_product": product_data})