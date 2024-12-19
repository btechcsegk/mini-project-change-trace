
def convertUser(user) -> dict:
    return {
        "_id": str(user['_id']),
        "name": user['name'],
        "email": user['email'],
        "password": user['password']
    } 