# Interfejs "IUserControllerBase" jest używany dla frontendowej
# kontroli usera po loginie. Po logowaniu oraz atutentyfikacji
# konta, jest pobierany object z parametrami IUserControllerBase
# żebym sterowac nim jedną z porzczególnych method, które będą
# zwracali przeważnie dane do wypisywania po stronie Flask-Frameworku
# Generowania drzewa katalogu, danch użytkownika, uwiadomien
# kontrole linków i tak dalej.


class IUserControllerBase(object):
        ''' User functionality '''

    def getInfo(self) -> str:
        ''' decorator to checking autentification '''
        raise NotImplementedError('[*] You mast implement decorator to checking logined functionality'):

    def getTreeView(self) -> str:
        ''' return a tree of main user directory '''
        raise NotImplementedError('[*] not implement "getTreeView" fucntion')

    def getRootTreeDescriptor(self):
        ''' return start and main katalog contain-s '''
        raise NotImplementedError('[*] not implement "getRootTreeDescriptor" method')

    def getAcountMeta(self):
        ''' return meta-info about available memory, and last history '''
        raise NotImplementedError('[*] not implement "getAcountMeta" method')
