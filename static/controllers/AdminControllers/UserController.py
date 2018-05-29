from static.classes.datacontroller.SQLController import SQLCloud
from datetime import date


class Controller(SQLCloud):

    def __init__(self):
        super(Controller, self).__init__()

    def do(self, argumnets) -> str:
        email = argumnets.email
        ban = argumnets.ban
        stat = argumnets.stat
        links = argumnets.links
        to_delete = argumnets.to_delete
        to_root = argumnets.to_root
        no_root = argumnets.no_root
        issetUser, idUser = False, 0
        try:
            issetUser, idUser = self._test_user(email)
            if(issetUser == False):
                return "Nie ma takiego użytkownika w bazie"
        except Exception as a:
            print(a)
            return "Nie ma takiego użytkownika w bazie"

        if(to_delete):
            function = self.delete("users")
            try:
                function(idUser=idUser)
                return "[*] Success! User by Email -{}- being removed".format(email)
            except:
                return "[!] Error!"
        elif(to_root):
            function = self.update("users")
            try:
                function(idUserType=2)(idUser=idUser)
                return "[*] Success! Now user by Email -{}- get root-access".format(email)
            except:
                return "[!] Error!"
        elif (no_root):
            function = self.update("users")
            try:
                function(idUserType=1)(idUser=idUser)
                return "[*] Success! Now user by Email -{}- get root-access".format(email)
            except:
                return "[!] Error!"
        elif(ban != 0):
            function = self.insert("banns")
            try:
                function(idUser, ban, date.today())
                return "[*] Success! User with Email -{}- banned".format(email)
            except Exception as s:
                return "[!] Error!"
        elif(links):
            return self._genLinkList(idUser)+self._getFilesLink(idUser)
        elif(stat):
            return self._getUserData(idUser) + self._getBans(idUser)+ self._getFilesLink(idUser)+self._genLinkList(idUser)
        else:
            return self._getUserData(idUser) + self._getBans(idUser) + self._getFilesLink(idUser) + self._genLinkList(idUser)

    def _test_user(self, email : str) -> tuple:
        select = self.select("users")
        value = select(google_email=email)
        wynik = True if len(select(google_email=email)) else False
        return wynik, 0 if wynik==False else value[0][0]

    def _genLinkList(self, userid : int):
        String = "{:-<50}\n\n".format("Active Links")
        findListOfLinkToUserId = self.select("linkLists")
        links = findListOfLinkToUserId(idUser=userid)
        if(len(links) > 0):
            onlyId = [linklist[2] for linklist in links]
            getLinkBy_IdLink = self.select("link")
            data = list(map(lambda x: getLinkBy_IdLink(idLink=x)[0], onlyId))[0]
            String = String + "Type:[{}] link:[{}] available[ TODO DATE ]\n".format(data[0], data[1])
        else:
            String = String + " - Empty\n"
        return String

    def _getFilesLink(self, userid: int):
        String = "{:-<50}\n\n".format("Files")
        wynik = self.merge(*("users", "idUser", "file", "idFile", "version"), where={ "file.idUser" : userid})
        if(len(wynik)>0):
            for enitity in wynik:
                noUser = enitity[10:]
                setOfIndex = [0, 4, 5, 6, 7, 8, 9]
                String=String+"Description:[{}] Version:[{}] HASH:[{}] Size:[{}] Extention:[{}] path[{}], accessType[{}]\n".format(*(noUser[x] for x in setOfIndex))
        else:
            String= String+" - Empty\n"
        return String

    def _getBans(self, userid: int):
        String = "{:-<50}\n\n".format("Ban-history")
        function = self.select("banns")
        bans = function(idUser=userid)
        if (len(bans) > 0):
            for x in bans:
                String = String + "Status:[{:>6}] Data:[{}]\n".format(x[2], x[3])
        else:
            String = String + " - Empty\n"
        return String

    def _getUserData(self, userid:int):
        String = "{:-<50}\n\n".format("User-Data")
        function = self.select("users")
        entity = function(idUser=userid)[0]
        String = String+"NickName:[{}]\nName:[{}]\nPublicKey:[{}]\nEmail:[{}]\n".format(entity[2], entity[5], entity[3], entity[6])
        return String


