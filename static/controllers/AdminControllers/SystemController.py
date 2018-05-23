from static.classes.datacontroller.SQLController import SQLCloud


class Controller(SQLCloud):

    def __init__(self):
        super(Controller, self).__init__()

    def do(self, argumnets) -> str:

        kusers = argumnets.users
        kfiles = argumnets.files
        kservers = argumnets.servers
        klogs = argumnets.logs
        return "[!] Function is not implement"

        """
        issetUser, idUser = False, 0
        try:
            issetUser, id = self._test_user(filename)
        except Exception as a:
            print(a)
            return "!"


        if(kusers):
            # TODO:
            function = self.delete("user")
            try:
                function(google_email="sergiy19981@gmail.com")
                print("[*] Success! User by Email -{}- being removed".format(email))
            except:
                print("[!] Error!")
        elif (kfiles):
            # TODO:
            function = self.update("userTypes")
            try:
                function(id="sergiy19981@gmail.com")
                print("[*] Success! Now user by Email -{}- get root-access".format(email))
            except:
                print("[!] Error!")
        elif(kservers):
            # TODO:
            function = self.update("userTypes")
            try:
                function(id="sergiy19981@gmail.com")
                print("[*] Success! Now user by Email -{}- get root-access".format(email))
            except:
                print("[!] Error!")
        elif(klogs):
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

    def _test_user(self, email : str) -> tuple:
        # TODO
        select = self.select("file")
        print("[{:^18}] Testing mail".format(self._test_user.__name__))
        value = select(google_email="sergiy19981@gmail.com")
        wynik = True if len(select(describe="sergiy19981@gmail.com")) else False
        return wynik, 0 if wynik == False else value[0][0]
        
    """