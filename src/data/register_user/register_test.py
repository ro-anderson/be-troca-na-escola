from faker import Faker
from src.infra.test import UserRepositorySpy
from .register import RegisterUser

faker = Faker()


def test_register():
    """ Testing registry method """

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.name(), "email": faker.name()}

    response = register_user.register(
        name=attributes["name"], email=attributes["email"]
    )

    # Testing inputs
    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["email"] == attributes["email"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_fail():
    """ Testing registry method in fail """

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {"name": faker.random_number(digits=2), "email": faker.name()}

    response = register_user.register(
        name=attributes["name"], email=attributes["email"]
    )

    print(response)

    # Testing inputs
    assert user_repo.insert_user_params == {}

    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
