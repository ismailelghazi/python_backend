def individual_serial(clients) -> dict:
    return {
        "id": str(clients["_id"]),
        "Cin": str(clients["Cin"]),
        "Assure": str(clients["Assure"])
    }

def list_serial(client) -> list:
    return [individual_serial(clients) for clients in client]