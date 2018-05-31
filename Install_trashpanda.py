import os

'''variables'''

directories = ["/srv/Data/",
               "/srv/DUMP",
               "/var/log/trashpanda/"]


'''
Tworzy wszystkie katalogi uwzględnione w tablicy *directories*
'''


def makedirs():
    for directory in directories:
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except:
                return 1
    return 0


def getPort():

    while True:
        try:
            PORT = int(input("Please enter prefered port to listen on: "))
        except ValueError:
            print("Sorry, the input was not valid, try again")
            continue
        else:
            break

    print("U chose port: " + str(PORT) + "\n")

    return PORT


'''
Pobieranie listy katalogów do zamontowania, zostaną przekazane do tablicy environ w celu zamontowania ich w dockerze
'''


def getMounts():

    print("Please, list directories you wish to mount into your docker container \n"
                      "(example: /dir1/ /example_dir/dir2/ ... \n")
    DIRS = list()

    while True:
        DIRECTORY = input("Podaj sciezke: np. /srv")

        if not testForExistence(DIRECTORY):
            if askForCreating():
                try:
                    os.makedirs(DIRECTORY)
                    DIRS.append(DIRECTORY)
                except:
                    print("Brak uprawnien, kurde \n")
            else:
                print("Tobie dupa")
        else:
            DIRS.append(DIRECTORY)

        if str(input("Would you like to mount more directories ? y/n \n"))[0] == "y":
            pass
        else:
            break

    return DIRS


'''
Test istnienia podanej ścieżki
'''


def testForExistence(GIVEN_DIR):

    if not os.path.exists(GIVEN_DIR):
        return False
    else:
        return True

'''
Zapytanie o utworzenie brakujących ścieżek
'''


def askForCreating():

    answer = str(input("Listed directions don't exist. \n"
                       "Do you wish to create them ? Otherwise all correct directories will be discarded \n"
                       "Type y to agree for creating mentioned directions \n"))
    if answer == "y":
        return True
    else:
        return False

'''
Zapytanie o pominięcie tworzenia błędnych ścieżek, oraz zamontowanie prawidłowych
'''


def askForSkip():
    answer = str(input("We couldn't have created some of given directories \n"
                       "Do you want to continiue without them ? y / n ? \n"))
    if answer == "y":
        return True
    else:
        return False

def askForRepo():
    return str(input("Podaj lokalne repozytorium docker'a \n"))

def startDocker(DIRS: list, port):
    docker_start = "sudo docker run -it -p "
    PORT = str(port) + ":5000 "

    mounted = ""
    for item in DIRS:
        mounted = mounted + "-v " + item + ":" + item + ":Z "

    repo = askForRepo()
    return docker_start + PORT + mounted + repo



''' MAIN '''

test = str(input("Would you like to use default configuration ? y/n"))
print("Status code tworzenia folderow: {0}".format(makedirs()))

if test != "y":
    PORT = str(getPort())
    DIRS = getMounts()
else:
    PORT = "80"
    DIRS = list()
    DIRS.append("/srv")
    DIRS.append("/var/log/trashpanda")

Command = startDocker(DIRS, PORT)
print(Command)
os.system(Command)

