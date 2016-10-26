import framework
import container

def sort_machine(x):
    return sorted(x, key=lambda k: k['price'])  

container = container.Container()
container.add_component(sort_machine)

fuku = container.resolve(framework.FruitBay)

fuku.add_fruit("Apple",12)
fuku.add_fruit("PineApple",1)
fuku.add_fruit("Grape",34)

print fuku.get_cheapest_fruit()
