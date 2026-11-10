from security import hash_password, verify_password


def test_hash_password():
    password = "password123"
    hashed = hash_password(password)

    assert password != hashed


def test_verify_password():
    password = "password123"
    hashed = hash_password(password)

    assert verify_password(password, hashed)
