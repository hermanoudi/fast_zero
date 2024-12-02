from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username="Hermano",
        email="hermano@teste.com",
        password="minha_senha_foda",
    )

    session.add(user)
    session.commit()

    # session.refresh(user)
    result = session.scalar(
        select(User).where(User.email == "hermano@teste.com")
    )

    assert result.id == 1
