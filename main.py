from framework import *
from container import *
from client_code import *

container = Container()
container.add_component(sort_machine)

fuku = container.resolve(FruitBay)

fuku.add_fruit("Apple",12)
fuku.add_fruit("PineApple",1)
fuku.add_fruit("Grape",34)

print fuku.get_cheapest_fruit()
