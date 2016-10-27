from framework import *
from container import *


container = Container()
# container.add_component("client_code","my_sort_machine","sort_machine")
container.register_from_config()

fuku = container.resolve(FruitBay)

fuku.add_fruit("Apple",12)
fuku.add_fruit("PineApple",1)
fuku.add_fruit("Grape",34)

print fuku.get_cheapest_fruit()
