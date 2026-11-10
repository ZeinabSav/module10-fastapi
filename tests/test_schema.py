import pytest
from pydantic import ValidationError

from schemas.user import UserCreate


def test_valid_user():

    user = UserCreate(
        username="john",
        email="john@example.com",
        password="password123"
    )

    assert user.username == "john"


def test_invalid_email():

    with pytest.raises(ValidationError):

        UserCreate(
            username="john",
            email="not-an-email",
            password="password123"
        )