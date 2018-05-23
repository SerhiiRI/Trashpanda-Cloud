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
        idUserType = "1"
        nickname = "Noob"
        publicKey = google_id
        DB = SQLCloud()
        DB_Insert = DB.insert("users")
        DB_Insert(idUserType, nickname.encode('UTF-8'), publicKey, google_id, full_name.encode('UTF-8'), google_email.encode('UTF-8'), google_token)
        return True

    else:
        return False

#print(Register("0ogvi9orr8na1ls7vbzrqfp7cf2", "1", "2", "3"))
