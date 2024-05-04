def individual_serial(Users) -> dict:
    return {
        "id": str(Users["_id"]),
        "email": str(Users["email"]),
        "password": str(Users["password"])
    }

def list_serial(user) -> list:
    return [individual_serial(Users) for Users in user]