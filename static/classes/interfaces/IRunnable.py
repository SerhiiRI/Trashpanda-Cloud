class IRunnable(object):

    def __init__(self):
        raise NotImplementedError

    def config(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError
