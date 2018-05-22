import os

'''variables'''

directories = ["/srv/Data/",
               "/srv/Data/DUMP/",
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

    MOUNT = str(input("Please, list directories you wish to mount into your docker container \n"
                      "separate them with whitespaces (example: /dir1/ /example_dir/dir2/ ... \n"))
    TEST_MOUNT = MOUNT.split(" ")
    not_existing = testForExistence(TEST_MOUNT)

    if len(not_existing) != 0:

        BAD_DIR = list()

        if askForCreating():

            for dirs in not_existing:
                try:
                    os.makedirs(dirs)
                except:
                    BAD_DIR.append(dirs)

            if len(BAD_DIR) > 0:
                if askForSkip():
                    for item in BAD_DIR:
                        TEST_MOUNT.remove(item)
                else:
                    return None
        else:
            return None

    MOUNT = ""

    for item in TEST_MOUNT:
        MOUNT = MOUNT + " " + item

    return MOUNT


'''
Test istnienia podanej ścieżki
'''


def testForExistence(GIVEN_LIST):

    not_existing = list()

    for smth in GIVEN_LIST:
        if not os.path.exists(smth):
            not_existing.append(smth)

    return not_existing

'''
Zapytanie o utworzenie brakujących ścieżek
'''


def askForCreating():

    answer = str(input("Some of listed directions don't exist. \n"
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


''' MAIN '''
print(makedirs())
print(str(getPort()))
print(getMounts())


