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
        print(argumnets)
        self._test_user(email)

    def _test_user(self, email : str) -> bool:
        select = self.like("users")
        print("[{:^18}] Testing mail".format(self._test_user.__name__))
        print(select(google_email="sergiy19981@gmail.com"))
        return True if len(select(google_email=email)) else False
