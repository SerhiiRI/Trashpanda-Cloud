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
    "id": random.randint(0, 10000),
    "fun": random.choice(["factorial", "bublesort", "searching"]),
    "machine": {
        "cpu": random.randint(0, 100) + 1,
        "disk": random.randint(0, 100) + 1,
        "ram": random.randint(0, 100) + 1
    },
    "function": {
        "factorial": random.randint(1, 100)+1,
        "bublesort": random.randint(1, 100)+1,
        "searching": random.randint(1, 100)+1
    },
}