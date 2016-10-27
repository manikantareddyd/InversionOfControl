from framework import *
from container import *

container = Container()
# container.add_component(module="client_code",component_name="my_sort_machine",dependency_name="sort_machine")
container.register_from_config()

fuku = container.resolve(FruitBay)

fuku.add_fruit("Apple",12)
fuku.add_fruit("PineApple",1)
fuku.add_fruit("Grape",34)

print fuku.get_cheapest_fruit()
