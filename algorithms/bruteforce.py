def bruteforce(things, weight_limit: int):
    if len(things) == 0:
        return 0, []
    #valor maximo fuerza bruta
    max_value = 0
    max_valued_packed = []
    for i, thing in enumerate(things):
        if thing.weight > weight_limit:
            continue

        value, packed = bruteforce(things[i + 1:], weight_limit - thing.weight)
        if value + thing.value >= max_value:
            max_value = value + thing.value
            max_valued_packed = [thing] + packed
    #regresa valores maximos y minimos acomodados
    return max_value, max_valued_packed
