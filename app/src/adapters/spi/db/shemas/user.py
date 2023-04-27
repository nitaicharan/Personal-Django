from pydantic import BaseModel


class UserShema(BaseModel):
    email: str
    token: str
    username: str
    bio: str
    image: str
    password: str
    createdAt: str
    updatedAt: str

    class Config:
        orm_mode = True
