"""

Login page API

"""

# Importing packages and modules
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

# Setting the template path
templates = Jinja2Templates(directory="sources/templates/pages")

# Setting the route
router = APIRouter(prefix="", tags=["index"])

# Rendering the login page
@router.post("/", response_class=HTMLResponse)
async def login():
    return templates.TemplateResponse("index.html")