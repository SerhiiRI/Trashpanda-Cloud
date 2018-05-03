"""
To musi być taki dlugi slownik dla statusKodów pod logi
Jak to sie liczy? Chm... dobre pytania...
żadnych pytan do reprezentacji

Autor: Serhii Riznychuk
"""


from static.tool.console.vt1000 import ForeGround, BackGround
# TODO: prosze o dodatkowych kluczach na każdy typ blędu... i zachuj mi nie ciekawi że to jest nudne...

STATUSCODE = {
    '01': {
        'type': 'error',
        'max': 4,
        'not_used': (2,4),
        'fcolor': ForeGround.blue,
        'bcolor': BackGround.red,
        # --------------------{only codes}------------------
        1: "Coś sie zjebalo",
        2: "Coś sie zakrzaczylo",
        3: "Ha! Jesteś gejem!",
        4: "Trzeba znależć jakiegoś kodera"
    },
    '02': {
        'type': 'critical',
        'max': 5,
        'not_used': (2,5),
        'fcolor': ForeGround.white,
        'bcolor': BackGround.red,
        # --------------------{only codes}------------------
        1: "Bo kurde już nie moge to pisać",
        2: "Ot i tworzysz tą architekuture",
        3: "I rozumiem że staram wynalezdz dzwi",
        4: "A we flasku to idzie odrębnym modulem",
        5: "tzn, że ktoś cos podobnego juz napisal"
    },
    '03': {
        'type': 'info',
        'max': 6,
        'not_used': (1, 2, 3, 4),
        'fcolor': ForeGround.white,
        'bcolor': BackGround.blue,
        # --------------------{only codes}------------------
        1: "Nie, nu normalnie potrzebuje jakiegóś niewolnika",
        2: "Czy mużyna... ja pierdole, może istnieje taka praca",
        3: "Że nawet placą tym liudziem który piszą tą ******",
        4: "dobra... dość póżno już jest, a ja tu musze coś napisąć",
        5: "no i pewnie nie chce tego zostawiać",
        6: "A wogle glodnym jestem... "
    },
    '04': {
        'type': 'warning',
        'max': 6,
        'not_used': (),
        'fcolor': ForeGround.black,
        'bcolor': BackGround.lightgrey,
        # --------------------{only codes}------------------
        1: "W loduwce nic nie ma... T_T zdechnie dzisiaj tu",
        2: "I niech na kamieniu pośmiertym napiszą: ",
        3: "\"Jego życia można opisać trzemia slówami:\"",
        4: '"Laseczki", "black Jack", "radość"',
        5: "ale to pojebane... nikt nie chce zarobić na takim",
        6: "Nie chce żyć"
    }
}