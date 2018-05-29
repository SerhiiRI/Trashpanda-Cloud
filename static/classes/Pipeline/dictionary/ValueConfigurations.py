constant_values = {
    '''
    Vartości statyczne ustalone wedlug potzeb server-a, dla
    systemowych komend load-balansingu. 
    Do agenta przychodzi lista z zadań funkcyj przkladowych
    (cp, mv, ls).
    '''
    "cp" : {
        "sizeMB": {
            "undo" : 0,
            "10" : 0.1,
            "100" : 0.2,
            "1000" : 0.3,
            "after" : 1
        },
        "pathCount" : {
            "1" : 0,
            "2" : 0.1,
            "3" : 0.2,
            "4" : 0.3,
            "*" : 1
        },
        "time-load": 0.4
    },
    "mv": {
        "sizeMB": {
            "5" : 0,
            "10" : 0.1,
            "100" : 0.2,
            "1000" : 1,
        },
        "pathCount" : {
            "1" : 0,
            "2" : 0.1,
            "3" : 0.2,
            "4" : 0.3,
            "*" : 1
        },
        "time-load": 0.1
    },
    "ls":{
        "sizeMB": "-",
        "pathCount": "-",
        "time-load": 1
    },
    '''
    Podane niżej wartości jest ustalonie w agentach, jak defoltowe 
    Po nich będzie sie skladać cala logika wyznacznia agentami pr-
    zyjąc zlecenia. 
    '''
    "cpu": {
        "load": {
            # Load percents
            "10%" : 0,
            "20%" : 0.5,
            "30%" : 0.9,
            "100%" : 1,
        },
        "temperature":{
            "90%": 0,
            "80%": 0.1,
            "70%": 0.2,
            "60%": 0.5,
            "50" : 1,
        }
    },
    "disk": {
        "load": {
            # Get random value of data outputTransfer
            # max, data load is 500 MB/s
            "10Mb/s" : 0,
            "50Mb/s" : 0.2,
            "100Mb/s": 0.5,
            "after" : 1,
        }
    },
    "ram": {
        "load":{
            "20%": 0,
            "50%": 0.7,
            "70%": 1,
        }
    },
}

