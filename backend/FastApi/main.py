from fastapi import FastAPI
from routers import basic_auth_users, jwt_auth_users, products, users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(users_db.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

# Recursos estaticos - Clase en video (14/12/2022): https://www.twitch.tv/videos/1679022882
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(): 
  return {"message": "¡Hola FastAPI!"}

@app.get("/url")
async def url():
  return { "url_curso": "https://mouredev.com/python" }

# Inicia el server uvicorn main:app --reload