# api paths:

### /users/get/{id} GET

    Params: None

---

    Returns(JSON):
    
    status: str <- [Success, User not exist]
    code: int <- [200, 404]

    status == Success ->
    {
        comments_id: list
        id: int
        mail: str
        name_id: int
        phone: str
        rating: float
        user_type: int
    }
---

---

### /users/get GET
    
    Params: None
---
    Returns(JSON):
    
    status: str <- [User table is empty, Success]
    code: int <- [404, 200]
    
    status == Success ->
    {
        users: list - list of users*
    }


 
    *user = {
        comments_id: list
        id: int
        mail: str
        name_id: int
        phone: str
        rating: float
        user_type: int
    }
---

---

### /user/put PUT

    Params(JSON):
    
    mail: str
    name_id: int
    phone: str
    rating: float
    user_type: int
    comments_id: list

---

    Returns(JSON):
    
    status: str <- [User exists, Bad request, Success]
    code: int <- [409, 400, 200]
---

---
### /user/delete/{user_id} DELETE
    Params: None
---
    Returns(JSON):

    status: str <- [Success, User not exist]
    code: int <- [200, 404]
---

---

### /name/put PUT

    Params(JSON):

    firstname: str
    lastname: str
    fathername: str

---

    Returns(JSON):
    
    status: str <- [Success, Bad request]
    code: int <- [200, 400]
    
    status == Success ->
    {
        name_id: int - name unique identifier to access the row
    }
---
