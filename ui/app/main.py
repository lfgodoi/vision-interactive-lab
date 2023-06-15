"""

Main file

"""

# Importing packages and modules
import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from sources.routers import login, index

# File info
__author__ = "Leonardo Godoi"
__date__ = "2023-06-15"

# Project info
title = "Vision Interactive Lab - UI"
description = "UI service backend"

# Setting the routes
router = APIRouter()
router.include_router(login.router)
router.include_router(index.router)

# Starting the app
app = FastAPI(title=title, description=description)

# Including the router in the app
app.include_router(router)

# Mounting the static files directory
app.mount("/static", StaticFiles(directory="sources/templates/static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)



