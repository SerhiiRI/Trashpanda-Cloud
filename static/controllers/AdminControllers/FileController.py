from static.classes.datacontroller.SQLController import SQLCloud


class Controller(SQLCloud):

    def __init__(self):
        super(Controller, self).__init__()

    def do(self, argumnets):
        filename = argumnets.filename
        kdelete = argumnets.to_delete
        klock = argumnets.to_lock
        kopen = argumnets.to_open

        return "[!] Function not implement"

        """
        issetUser, idUser = False, 0
        try:
            issetUser, id = self._test_user(filename)
        except Exception as a:
            print(a)
            print("Coś sie zjebalo!")
            return False

        if(kdelete):
            # TODO:
            function = self.delete("user")
            try:
                function(google_email="sergiy19981@gmail.com")
                print("[*] Success! User by Email -{}- being removed".format(email))
            except:
                print("[!] Error!")
        elif(klock):
            # TODO:
            function = self.update("userTypes")
            try:
                function(id="sergiy19981@gmail.com")
                print("[*] Success! Now user by Email -{}- get root-access".format(email))
            except:
                print("[!] Error!")
        elif(kopen):
            # TODO:
            function = self.insert("bann")
            try:
                function(idUser, date.today())
                print("[*] Success! User with Email -{}- banned".format(email))
            except:
                print("[!] Error!")
        else:
            # TODO: napisać funkacje dla linków
            function = self.select("links")
            try:
                function(google_email="sergiy19981@gmail.com")
                print("[*] Success! User by Email -{}- being removed".format(email))
            except:
                print("[!] Error!")
        """
