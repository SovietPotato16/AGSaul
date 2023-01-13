from algorithms.genetic import Genome
from collections import namedtuple
#import matplotlib.pyplot as plt


Thing = namedtuple('Thing', ['name', 'value', 'weight'])

first_example = [
    Thing('Carpeta', 151, 251),
    Thing('Cartera', 75, 26),
    Thing('Calculadora', 648, 482),
    Thing('Libros', 527, 183),
    Thing('Balon', 230, 155),
]

second_example = [
    Thing('Saco de box', 30, 250),
    Thing('Medicina', 15, 90,),
    Thing('Telescopio', 300, 400),
    Thing('Zapatos', 110, 100),
    Thing('Mouse', 800, 200),
    Thing('Luces', 35, 460),
    Thing('Rifle', 900, 850),
    Thing('Casa de campania', 1300, 5303),
    Thing('Botas', 80, 150),
    Thing('Botellas', 15, 25),
    Thing('Basura', 10, 10),
    Thing('Papel', 90, 80),
    Thing('Diario', 100, 700),
    Thing('Camara', 100, 70),
    Thing('Pelota', 999, 150),
    Thing('Carbon', 1512, 151),
    Thing('Vendaje', 91, 15),
    Thing('Cania', 193, 193),
    Thing('Perfume', 581, 619),
    Thing('Pistola', 890, 900),
    Thing('RadioSatelital', 100, 500),
    
] + first_example


def generate_things(num: int) -> [Thing]:
    return [Thing(f"thing{i}", i, i) for i in range(1, num+1)]


def fitness(genome: Genome, things: [Thing], weight_limit: int) -> int:
    if len(genome) != len(things):
        raise ValueError("genome and things must be of same length")
    weight = 0
    value = 0
    for i, thing in enumerate(things):
        if genome[i] == 1:
            weight += thing.weight
            value += thing.value

            if weight > weight_limit:
                return 0

    return value


def from_genome(genome: Genome, things: [Thing]) -> [Thing]:
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing]
    print (result)

    return result


def to_string(things: [Thing]):
    return f"[{', '.join([t.name for t in things])}]"


def value(things: [Thing]):
    return sum([t.value for t in things])


def weight(things: [Thing]):
    return sum([p.weight for p in things])


def print_stats(things: [Thing]):
    print(f"Cosas: {to_string(things)}")
    print(f"Valor {value(things)}")
    print(f"Peso: {weight(things)}")

def plot():
    print_stats("Cosas",generation, peso, value)
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing]
    print (result)
    
    