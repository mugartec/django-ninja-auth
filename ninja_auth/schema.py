from django.contrib.auth import get_user_model
from ninja import Schema
from ninja.orm import create_schema
from typing import Dict, List


UserOut = create_schema(
    get_user_model(),
    exclude=['password']
)


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
