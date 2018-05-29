import threading

class Process(threading.Thread):

    def __init__(self, func):
        self.function = func
        # self.parameter = values
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.function(5)
        except RuntimeError as message:
            print("[!] Bląd krytyczny")
            print(message)
        except Exception as message:
            print("[!] Wyjątek!")
            print(message)
