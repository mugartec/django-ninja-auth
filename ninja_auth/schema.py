from ninja import Schema
from typing import Dict, List


class UserOut(Schema):
    id: int
    username: str
    email: str


class LoginIn(Schema):
    username: str
    password: str


class RequestPasswordResetIn(Schema):
    email: str


class SetPasswordIn(Schema):
    username: str
    new_password1: str
    new_password2: str
    token: str


class ChangePasswordIn(Schema):
    old_password: str
    new_password1: str
    new_password2: str


class ErrorsOut(Schema):
    errors: Dict[str, List[str]]
