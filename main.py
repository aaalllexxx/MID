import random

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse
from models import *
from database import *

app = FastAPI()

Base.metadata.create_all(engine)

# ссылки на видео с youtube kids
videos = [
    "https://www.youtube.com/watch?v=1Ux_5-rWl4U",
    "https://www.youtube.com/watch?v=ZufF9hrRU_8",
    "https://www.youtube.com/watch?v=czt5mFOPhoY",
    "https://www.youtube.com/watch?v=lf5p2P7GMvo",
    "https://www.youtube.com/watch?v=JEg6iXxrLfk",
    "https://www.youtube.com/watch?v=ooU2Kz5iBcQ",
    "https://www.youtube.com/watch?v=SnDfhUsNIxo",
    "https://www.youtube.com/watch?v=fvl1_VvslQ0",
    "https://www.youtube.com/watch?v=UWkZ5aQyLHQ",
    "https://www.youtube.com/watch?v=t_qSAcZ_Hps"
]


# основная страница API
@app.get("/")
async def root():
    # редирект на рандомное видео из списка
    return RedirectResponse(random.choice(videos))


@app.get("/users/get/{user_id}")
async def get_users_by_id(request: Request, user_id: int):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        return json.loads(str(user))
    return {"status": "User not exist", "code": 404}


@app.get("/users/get")
async def get_users(request: Request):
    users = session.query(User).all()
    users = json.dumps([json.loads(str(user)) for user in users])
    if users:
        return {"users": json.loads(users), "status": "Success", "code": 200}
    return {"status": "Users table is empty", "code": 404}


@app.put("/users/put")
async def put_users(request: Request):
    data = await request.json()
    mail = data.get("mail")
    comments_id = json.dumps(data.get("comments_id"))
    name_id = data.get("name_id")
    phone = data.get("phone")
    rating = data.get("rating")
    user_type = data.get("user_type")
    if mail and name_id and phone and rating and user_type and comments_id:
        user = User(mail=mail, comments_id=comments_id, name_id=name_id, phone=phone, rating=rating,
                    user_type=user_type)
        if not session.query(User).filter_by(phone=phone).first():
            session.add(user)
            session.commit()
            return {"status": "Success", "code": 200}
        return {"status": "User exists", "code": 409}
    return {"status": "Bad request", "code": 400}


@app.delete("/users/delete/{user_id}")
async def delete_user(request: Request, user_id: int):
    user = session.query(User).filter_by(id=user_id)
    if user.first():
        user.delete()
        session.commit()
        return {"status": "Success", "code": 200}
    return {"status": "User not exist", "code": 404}


@app.put("/name/put")
async def put_name(request: Request):
    data = await request.json()
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    fathername = data.get("fathername")
    if firstname and lastname and fathername:
        name = Name(firstname=firstname, lastname=lastname, fathername=fathername)
        session.add(name)
        session.commit()
        return {"status": "Success", "code": 200, "name_id": name.id}
    return {"status": "Bad request", "code": 400}


@app.get("/cities/get/{city_id}")
async def get_city(city_id: int):
    city = session.query(City).filter_by(id=city_id).first()
    if city:
        return json.loads(str(city))
