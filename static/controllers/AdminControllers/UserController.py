from static.classes.datacontroller.SQLController import SQLCloud


class Controller(SQLCloud):

    def __init__(self):
        SQLCloud.__init__(self)

    def do(self, argumnets):
        email = argumnets.email
        ban = argumnets.ban
        stat = argumnets.stat
        links = argumnets.links
        to_delete = argumnets.to_delete
        to_root = argumnets.to_root
        self._test_user(email)
        if(to_delete):
            function = self.delete("user")
            try:
                function(google_email="sergiy19981@gmail.com")
                print("[*] Success! User by Email -{}- being removed".format(email))
            except:
                print("[!] Error!")
        elif(to_root):
            function = self.update("userTypes")
            try:
                function(id="sergiy19981@gmail.com")
                print("[*] Success! User by Email -{}- being removed".format(email))
            except:
                print("[!] Error!")
        elif(ban):
            try:
                function(google_email="sergiy19981@gmail.com")
                print("[*] Success! User by Email -{}- being removed".format(email))
            except:
                print("[!] Error!")
        elif(links):
            try:
                function(google_email="sergiy19981@gmail.com")
                print("[*] Success! User by Email -{}- being removed".format(email))
            except:
                print("[!] Error!")
        elif(stat):
            try:
                function(google_email="sergiy19981@gmail.com")
                print("[*] Success! User by Email -{}- being removed".format(email))
            except:
                print("[!] Error!")
        else:
            try:
                function(google_email="sergiy19981@gmail.com")
                print("[*] Success! User by Email -{}- being removed".format(email))
            except:
                print("[!] Error!")

    def _test_user(self, email : str) -> bool:
        select = self.select("users")
        print("[{:^18}] Testing mail".format(self._test_user.__name__))
        return True if len(select(google_email="sergiy19981@gmail.com")) else False
