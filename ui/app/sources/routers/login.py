"""

Login page API

"""

# Importing packages and modules
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# Setting the template path
templates = Jinja2Templates(directory="sources/templates/pages")

# Setting the route
router = APIRouter(prefix="/login", tags=["login"])

# Login form model
class LoginForm(BaseModel):
    username: str
    password: str

# Authentication response model
class ResponseAuthentication(BaseModel):
    success: bool

# Rendering the login page
@router.post("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# User authentication
@router.post("/authenticate", response_model=ResponseAuthentication)
async def login(login_form: LoginForm):
    return templates.TemplateResponse("login.html")