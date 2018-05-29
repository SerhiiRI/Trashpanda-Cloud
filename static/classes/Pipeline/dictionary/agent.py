import random
agent = {
    # Przy poprawnej realizacji wartość tego pola musi definiować
    # progama automatycznie, zależąć od tego, o jakiej specyfika-
    # cji wymagań agenta byla zrobiono. Tzn, zrozumienie proceśów
    # wykonwczych.
    # Np. jeżeli agent jest uzależniony węwnątrz od czasu, to wt-
    # edy musi sie wyliczyć odpowiednią wagę wychodzącą, obojętne
    # jaka ta waga będzie miala znaczenia.
    # W programie te wartośći wypelnia mega-inteligentna funkcja
    # random((range(0,101, 1)))
    "info": {
        "id": random.randint(0, 10000),
    },
    "machine": {
        "cpu": random.randint(0, 101),
        "disk": random.randint(0, 101),
        "ram": random.randint(0, 101),
    },
    "function": {
        "factorial": random.randint(0, 101),
        "ls": random.randint(0, 101),
        "mv": random.randint(0, 101)
    },
    "price": 0
}