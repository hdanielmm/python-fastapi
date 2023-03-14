from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["users"])

#Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

user_list = [
    User(id=1, name="Daniel", surname="Marin", url="https://daniel.com", age=39),
    User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=39),
    User(id=3, name="Haakon", surname="Dahlberg", url="https://haakon.com", age=39)
]

@router.get("/usersjson")
async def usersjson():
    return [
        {"name": "Daniel", "surname": "Marin", "url": "http://danielo.com", "age": 39},
        {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 35},
        {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]

@router.get("/users")
async def users():
    return user_list

# Path
@router.get("/user/{id}")
async def user(id: int):
    return search_query(id)

# Query
@router.get("/user/")
async def user(id: int):
    return search_query(id)
    
@router.post("/user/", response_model=User, status_code=201)
async def add_user(user: User):
    if type(search_query(user.id)) == User:
        raise HTTPException(status_code=404, detail="El id ya existe")
    else:
        user_list.append(user)
    return user

@router.put('/user/')
def put_user(user: User):
    found: bool = False

    for (index, saved_user) in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    
    if not found:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    return {"updated_user": user}

@router.delete('/user/{id}', status_code=204)
async def delete_user(id: int):
    found: bool = False

    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
    
    if not found:
        raise HTTPException(status_code=404, detail="No se ha encontrado el usuario")
    else:
        return {"Eliminado": True}

def search_query(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=404, detail="No se ha encontrado al usuario")
    