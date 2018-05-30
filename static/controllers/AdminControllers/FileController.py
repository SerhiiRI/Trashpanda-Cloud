from static.classes.datacontroller.SQLController import SQLCloud
import datetime


class Controller(SQLCloud):

    def __init__(self):
        super(Controller, self).__init__()

    def do(self, argumnets):
        filename = argumnets.filename
        kdelete = argumnets.to_delete
        kuser = argumnets.users
        kstat = argumnets.stat
        kversion = argumnets.version
        klock = argumnets.to_lock

        issetFile, idFile = False, 0

        issetFile, idFile = self.__test_file(filename)
        if(idFile!=0):
            self.__getInfo(idFile)
        else:
            return "File not found"
        if(kstat):
            view = ""
            if (kversion == False):
                view += self._print_linklist() + self._print_userdata() + self._print_versions_list()
            else:
                view += self._print_linklist(kversion) + self._print_userdata() + self._print_versions_list(
                    kversion)
            return view
        elif(klock and kversion != False):
            update = self.update('link')
            try:
                filtered = list(filter(lambda version: str(kversion) == str(version[1]), self._link_list))
                for idlink in filtered:
                    update(available=datetime.datetime(1, 1, 1))(idLink=idlink[-1])
            except Exception as a:
                return "Empty links to version-file"
        elif(kdelete):
            if (kversion == False):
                delete_file = self.delete('file')
                try:
                    delete_file(idFile=idFile)
                    return "Success removing file"
                except:
                    return "DataBase error"
            else:
                delete_file = self.delete('version')
                try:
                    delete_file(idFile=idFile, version=kversion)
                    return "Success removing version"
                except:
                    return "DataBase error"
        elif(kuser):
            return self._print_userdata()
        else:
            view = ""
            if (kversion == False):
                view += self._print_linklist() + self._print_userdata() + self._print_versions_list()
            else:
                view += "----"+self._print_linklist(kversion) + self._print_userdata() + self._print_versions_list(kversion)
            return view

    def __test_file(self, description):
        select = self.select("file")
        value = select(description=description)
        wynik = True if len(value) > 0 else False
        return wynik, 0 if wynik == False else value[0][0]

    def __getInfo(self, idFile):
        # get versions information
        SQL_select_versions = self.select('version')
        SQL_select_file = self.select('file')
        SQL_select_users = self.select('users')



        self._list_versions = SQL_select_versions(idFile=idFile)
        self._idversions_idFile = [(x[0], x[1]) for x in self._list_versions]        # get ownetrs
        _, self.idUser, self.description = SQL_select_file(idFile=idFile)[0]
        idUser, _, nickname, public_key, _, full_name, google_mail, _ = SQL_select_users(idUser=self.idUser)[0]
        self._userdata = (full_name, nickname, google_mail, public_key)
        # get path info,
        linklist = list()
        for x in self._idversions_idFile:
            s = self.merge("version", "idVersion", "linkLists", "idLink", "link", where={"version.idVersion": x[0]})
            if(len(s) > 0):
                linklist.append(s[0])
        # _link_list = lisst(...Tuple( idVersion, version, type, link, available, idLink))
        self._link_list = [(x[0], x[2], x[-3], x[-2], x[-1], x[-4]) for x in linklist]
        # _link_list = list( ( idVersion, idLinkList, idLink )
        self._id_link_list = [(x[0], x[11], x[12]) for x in linklist]
        # get tags tatg
        taglist = self.merge("file","idFile", "tags", "idTag", "tag")
        self._taglist = [x[-1] for x in taglist]

    def _print_versions_list(self, v=-1):
        String = "#{:<50}\n\n".format("Version List")
        finalLIst = self._list_versions
        if (int(v) > 0):
            finalLIst = filter(lambda x: str(x[2]) == str(v), self._list_versions)
        for x in finalLIst:
            _, _, version, hashsum, size, extention, path, accessType, _, timeCreate, timeAcces = x
            String = String+"Version:[{}], hashsum[{}], size[{}], extention[{}], path[{}], Access-Type: [{}], Dates(create/access): [{}] / [{}]\n".format(version, hashsum, size, extention, path, accessType, timeCreate, timeAcces)
        return String

    def _print_userdata(self, user=""):
        String = "#{:50}\n\n".format("Owner")
        data = self._userdata if(user=="") else filter(lambda x: str(x[2])==user, self._userdata)
        String = String + "Name:[{}], Nickname:[{}], Mail[{}], PubKey:[{}]\n".format(data[0], data[1], data[2], data[3])
        return String

    def _print_linklist(self, v=-1):
        String ="#{:<50}\n\n".format("Link-List")
        finalList = self._link_list if  int(v) < 0 else filter((lambda x: str(x[1]) == str(v)), self._link_list)
        for x in finalList:
            String += "Version:[{}], Type:[{}], Link[{}], available[{}]\n".format(*x[1:-1])
        return String