class FruitBayTraditional:
    def __init__(self):
        self.fruits = []

    def add_fruit(self,fruit_name,fruit_price):
        self.fruits.append({'name':fruit_name,'price':fruit_price})

    def get_cheapest_fruit(self):
        sorted_fruits = sorted(self.fruits, key=lambda k: k['price'])
        return sorted_fruits[0]['name']
