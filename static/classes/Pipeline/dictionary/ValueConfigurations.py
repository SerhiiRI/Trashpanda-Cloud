constant_values = {
    "compatible":{
        "low" : lambda x : False if x < 30 else True,
        "middle": lambda x : False if x < 60 else True,
        "high": lambda x : False if x < 85 else True,
    }
}

