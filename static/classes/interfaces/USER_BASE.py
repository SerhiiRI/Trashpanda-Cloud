# Implementowania dekoratorów, za pomącą których
# będą realizowane metody dostępu do funkcyjności
# przez ściślie określione uprawnienia od użytkownika,
# przez odczytania go stanu logowania w sessi, kuki i t.d.


class IPermission(object):
    ''' interface IUserBase creating for implementation functionality for user-s nanagement '''

    def rootPermision(self):
        ''' decorator to using only Cloud ROOT permision '''
        raise NotImplementedError('[*] class '+self.name+' not contain \nimplementation to rootPermision method')

    def login(self):
        ''' decorator to checking autentification '''
        raise NotImplementedError('[*] You mast implement decorator to checking logined functionality')

    def addUser(self, login : str, NickName : str) -> bool:
        ''' Function for add user to '''
        raise NotImplementedError('[*] not implement function "addUser"')

    def delUser(self, login : str) -> bool:
        ''' Function to removing user from '''
        raise NotImplementedError('[*] not implement function "delUser"')
