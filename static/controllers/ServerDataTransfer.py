# Interface to controll server

class ServerDataTransfer(object):
    ''' managing of data transfering '''

    __SERVER_LOCK = 0

    def upload(self):
        raise NotImplementedError('[*] not implement upload')

    def download(self):
        raise NotImplementedError('[*] not implement download')

    def lock(self, id: str) -> int:
        ''' if transmission of data mast be blocked for user '''
        ''' set user in blockList with status and timeStamp '''
        raise NotImplementedError('[*] not implement download')


    def setLockServer(self, status : int) -> bool:
        ''' lock for server '''
        self.__SERVER_LOCK = status
        return True

    def getLockServer(self):
        return False if self.__SERVER_LOCK == 0 else True
