from static.classes.datacontroller.SQLController import SQLCloud

def isRegistered(google_id) -> bool:
    DB = SQLCloud()
    select = DB.select("users")
    if len(select(google_id=google_id)) > 0:
        return True
    else:
        return False


def Register(google_id : str, full_name : str, google_email : str, google_token : str) -> bool:
    if (not isRegistered(google_id)):
        idUserType = 1
        nickname = "Noob"
        publicKey = google_id

        DB = SQLCloud()
        DB_Insert = DB.insert("users")
        DB_Insert(idUserType, nickname, publicKey, google_id, full_name, google_email, google_token)
        return True

    else:
        return False

