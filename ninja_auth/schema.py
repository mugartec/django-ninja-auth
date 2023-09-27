from django.contrib.auth import get_user_model
from ninja import Schema
from ninja.orm import create_schema
from typing import Dict, List
from .settings import USER_EXCLUDE_FIELDS

UsernameSchemaMixin = create_schema(
    get_user_model(),
    fields=[get_user_model().USERNAME_FIELD]
)

EmailSchemaMixin = create_schema(
    get_user_model(),
    fields=[get_user_model().EMAIL_FIELD]
)

UserOut = create_schema(
    get_user_model(),
    exclude=USER_EXCLUDE_FIELDS
)


class LoginIn(UsernameSchemaMixin):
    password: str


class RequestPasswordResetIn(EmailSchemaMixin):
    pass


class SetPasswordIn(UsernameSchemaMixin):
    new_password1: str
    new_password2: str
    token: str


class ChangePasswordIn(Schema):
    old_password: str
    new_password1: str
    new_password2: str


class ErrorsOut(Schema):
    errors: Dict[str, List[str]]
