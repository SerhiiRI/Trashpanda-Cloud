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
            print()
        elif(to_root):
            print()
        elif(ban):
            print()
        elif(links):
            print()
        elif(stat):
            print()
        else:
            print("[*] Nie dziala komenda ")

    def _test_user(self, email : str) -> bool:
        inf = self.select(nickname="costam")

        select = self.select("users")

        print("[{:^18}] Testing mail".format(self._test_user.__name__))
        return True if len(select(google_email="sergiy19981@gmail.com")) else False
