from pydantic import BaseModel, constr


# Authentication DataBase Model
class Authentication(BaseModel):
    user_id: int
    username: constr(regex="^[a-z0-9_-]{3,15}$")
    email: constr(Regex="[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")
    phone: constr(Regex="^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$")
    password: str

# model attributes with validations
